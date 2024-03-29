import pathlib
import gitlab_ci_docs.cli


def run_cli():
    ci_file_path = pathlib.Path(__file__).parent / 'pipl.yml'
    gitlab_ci_docs.cli.run(ci_file_path)
