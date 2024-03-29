import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'src'))

import argparse
import unittest
import importlib
import test_cli


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cli', action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    if args.cli:
        test_cli.run_cli()
    else:
        excludes = []

        is_test_case = lambda v: isinstance(v, type) and issubclass(v, unittest.TestCase) and not v.__name__.startswith('Base')

        py_items = pathlib.Path(__file__).resolve().parent.glob('test_*.py')
        testmodules = [importlib.import_module(str(i.stem)) for i in py_items if i.is_file()]
        testcases = [a for m in testmodules for a in [getattr(m, i) for i in dir(m)] if is_test_case(a)]

        suite = unittest.TestSuite([unittest.makeSuite(t) for t in set(testcases)])
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
