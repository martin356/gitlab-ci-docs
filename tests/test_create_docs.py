import pathlib
import gitlabcidocs
from pprint import pprint


def run_create_docs():
    ci_file_path = pathlib.Path(__file__).parent / 'pipl.yml'
    docs_file_path = pathlib.Path(__file__).parent / 'readme.test.md'
    docs = gitlabcidocs.create_docs(ci_file_path, docs_file_path)

    pprint(docs)
