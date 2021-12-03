"""{{ cookiecutter.project_name }} file for ensuring the package is executable
as `{{ cookiecutter.repo_name }}` and `python -m {{ cookiecutter.python_package }}`
"""
from pathlib import Path

from kedro.framework.project import configure_project

from .cli import run


def main():
    configure_project(Path(__file__).parent.name)
    run()


if __name__ == "__main__":
    main()
