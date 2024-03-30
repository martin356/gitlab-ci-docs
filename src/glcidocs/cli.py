from pathlib import Path
from typing import List
from glcidocs.pipelineparser import CiFileParser
from glcidocs.docsgen import HTMLBuilder


def read_doc_file(file_path: str|Path) -> List[str]:
    with open(file_path, 'r') as f:
        return [line for line in f]


def write_doc_file(file_path: str|Path, data: str) -> None:
    with open(file_path, 'w') as f:
        f.write(data)


def run(ci_file_path: str|Path, doc_file_path: str|Path) -> str:
    workflow = CiFileParser(ci_file_path).workflow
    docs = HTMLBuilder(workflow).docs

    docs_token = '<!--PIPELINE_DOCS-->'

    begin_docs_line_idx = None
    end_docs_line_idx = None

    out_lines = read_doc_file(doc_file_path)

    for i in range(len(out_lines)):
        if docs_token in out_lines[i]:
            if begin_docs_line_idx is None:
                begin_docs_line_idx = i
            else:
                end_docs_line_idx = i

    if begin_docs_line_idx is None:
        out_lines.insert(0, f'{docs_token}\n{docs}\n{docs_token}\n\n')
    elif end_docs_line_idx is None:
        out_lines.insert(begin_docs_line_idx+1, f'{docs}\n{docs_token}\n\n')
    else:
        out_lines = out_lines[:begin_docs_line_idx+1] + [docs+'\n'] + out_lines[end_docs_line_idx:]

    write_doc_file(doc_file_path, ''.join(out_lines))

    return docs
