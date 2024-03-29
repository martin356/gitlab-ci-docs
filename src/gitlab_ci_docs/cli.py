from pathlib import Path
from gitlab_ci_docs.pipelineparser import CiFileParser
from gitlab_ci_docs.docsgen import HTMLBuilder


def run(ci_file_path: str|Path):
    workflow = CiFileParser(ci_file_path).workflow
    html = HTMLBuilder(workflow)

    from pprint import pprint
    pprint(html.docs)
