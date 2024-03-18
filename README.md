[![PyPI version](https://badge.fury.io/py/package_name.svg)](https://badge.fury.io/py/package_name)
[![Conda-Forge version](https://img.shields.io/conda/vn/conda-forge/package_name)](https://anaconda.org/conda-forge/package_name)
[![Build status](https://github.com/github_username/package_name/actions/workflows/ci.yaml/badge.svg)](https://github.com/github_username/package_name/actions/workflows/ci.yaml)
[![Documentation Status](https://readthedocs.org/projects/package_name/badge/?version=latest)](https://package_name.readthedocs.io/en/latest/?badge=latest)

A Python package template.

- Building, publishing, and development environment managed by [Hatch](https://hatch.pypa.io/latest/)
- Linting and formatting by [Ruff](https://docs.astral.sh/ruff/) (via [pre-commit](https://pre-commit.com/))
- Type checking by [mypy](https://mypy-lang.org/)
- CI by [Github Actions](https://github.com/features/actions)
- Docs by [mkdocs](https://www.mkdocs.org/), hosted on [ReadTheDocs](https://about.readthedocs.com/)
- MIT licensed

## Setup

1. Find + replace `package_name` with package name. Rename `src/package_name` folder.
2. Find + replace `My Name` with author name in the LICENSE and `pyproject.toml`.
3. Find + replace `github_username` with Github username in the README, `mkdocs.yml`, and `pyproject.toml`.
2. Modify package description, dependencies, etc. in `pyproject.toml`.
3. Modify repository name and URL in `docs/mkdocs.yml` and `pyproject.toml`.
4. Adjust supported Python versions in `pyproject.toml` and `.github/workflows/ci.yaml`
5. Delete `src/package_name/main.py` and `tests/test_template.py`.

## Developing

See CONTRIBUTING.md for development instructions.