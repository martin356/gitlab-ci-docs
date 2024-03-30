import pathlib
import glcidocs.cli
from pprint import pprint


def run_cli():
    ci_file_path = pathlib.Path(__file__).parent / 'pipl.yml'
    docs_file_path = pathlib.Path(__file__).parent / 'readme.test.md'
    docs = glcidocs.cli.run(ci_file_path, docs_file_path)

    pprint(docs)
