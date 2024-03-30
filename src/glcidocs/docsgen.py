from typing import List, Dict
from glcidocs.pipelineparser import Workflow, Rule


class HTMLBuilder:

    columns_headers = ['Trigger', 'Variable', 'Required', 'Type', 'Choices', 'Default']

    def __init__(self, workflow: Workflow):
        self._docs = self.table(self.columns_headers, workflow.rules)

    @property
    def docs(self) -> str:
        return self._docs

    def create_rule_rows(self, rule: Rule) -> str:
        first_row = self.row([
            {'value': f'if: {rule.condition}', 'rowspan': len(rule.variables)},
            {'value': rule.variables[0].name},
            {'value': rule.variables[0].required_str},
            {'value': rule.variables[0].typename if rule.variables[0].typename else '-'},
            {'value': rule.variables[0].choices_str if rule.variables[0].choices_str else '-'},
            {'value': rule.variables[0].value}
        ])
        other_rows = '\n'.join([self.row([
            {'value': v.name},
            {'value': v.required_str},
            {'value': v.typename if v.typename else '-'},
            {'value': v.choices_str if v.choices_str else '-'},
            {'value': v.value}
        ]) for v in rule.variables[1:]])

        return first_row + other_rows

    def table(self, headers: List[str], rules: List[Rule]) -> str:
        return '\n'.join([
            '<table>',
            self.headers(headers),
            '\n'.join([self.create_rule_rows(r) for r in rules]),
            '</table>'
        ])

    def headers(self, headers: List[str]) -> str:
        return f'<tr>{"".join([f"<th>{h}</th>" for h in headers])}</tr>'

    def row(self, data: List[Dict[str, str]]) -> str:
        return f'<tr>{"".join([self.cell(v["value"], v.get("rowspan", None)) for v in data])}</tr>'

    def cell(self, value: str, rowspan=None) -> str:
        rowspan = f' rowspan="{rowspan}"' if rowspan and rowspan > 1 else ''
        return f'<td{rowspan}>{value}</td>'
