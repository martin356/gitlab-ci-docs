import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import argparse
import docsgen


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ci-file', required=False, default='.gitlab-ci.yml', help='Path to gitlab-ci.yml')
    parser.add_argument('--doc-file', required=False, default='README.md', help='Path to the file in the docs are injected to')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    docsgen.create_docs(args.ci_file, args.doc_file)
