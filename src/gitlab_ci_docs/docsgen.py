from typing import List
from gitlab_ci_docs.pipelineparser import Workflow


class HTMLBuilder:

    columns_headers = ['Trigger', 'Variable', 'Choices', 'Default', 'Type']

    def __init__(self, workflow: Workflow):
        self._docs = self.table(self.columns_headers, [])

    @property
    def docs(self) -> str:
        return self._docs

    def table(self, headers: List[str], rows: List[List[str]]) -> str:
        return '\n'.join([
            '<table>',
            self.headers(headers),
            '</table>'
        ])

    def headers(self, headers: List[str]) -> str:
        return f'<tr>{"".join([f"<th>{h}</th>" for h in headers])}</tr>'

    def row(self, data: List[str]) -> str:
        return f'<tr>{"".join([self.cell(v) for v in data])}</tr>'

    def cell(self, value: str) -> str:
        return f'<td>{value}</td>'
