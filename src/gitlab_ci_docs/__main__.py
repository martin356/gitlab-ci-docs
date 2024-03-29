import argparse
import gitlab_ci_docs.cli


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ci-file', required=False, default='gitlab-ci.yml', help='Path to gitlab-ci.yml')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    gitlab_ci_docs.cli.run(args.ci_file)
