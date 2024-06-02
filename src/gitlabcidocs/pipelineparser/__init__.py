from ruamel.yaml import YAML
from pipelineparser.workflow import Workflow


class CiFileParser:

    def __init__(self, filepath: str):
        with open(filepath) as f:
            self._pipeline = YAML().load(f)

    def get_workflow(self, include_all_rules: bool) -> Workflow:
        return Workflow(self._pipeline['workflow'], include_all_rules)
