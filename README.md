[![PyPI version](https://badge.fury.io/py/PACKAGE_NAME.svg)](https://badge.fury.io/py/PACKAGE_NAME)
[![Conda-Forge version](https://img.shields.io/conda/vn/conda-forge/PACKAGE_NAME)](https://anaconda.org/conda-forge/PACKAGE_NAME)
[![Build status](https://github.com/GITHUB_USERNAME/PACKAGE_NAME/actions/workflows/ci.yaml/badge.svg)](https://github.com/GITHUB_USERNAME/PACKAGE_NAME/actions/workflows/ci.yaml)
[![Documentation Status](https://readthedocs.org/projects/PACKAGE_NAME/badge/?version=latest)](https://PACKAGE_NAME.readthedocs.io/en/latest/?badge=latest)

A Python package template.

- Building, publishing, and development environment managed by [Hatch](https://hatch.pypa.io/latest/)
- Linting and formatting by [Ruff](https://docs.astral.sh/ruff/) (via [pre-commit](https://pre-commit.com/))
- Type checking by [mypy](https://mypy-lang.org/)
- CI by [Github Actions](https://github.com/features/actions)
- Docs by [mkdocs](https://www.mkdocs.org/), hosted on [ReadTheDocs](https://about.readthedocs.com/)
- MIT licensed

## Setup

1. Run `rm -rf .git && git init` to replace the template Git history with a new Git project.
2. Run `python -m init` to set package metadata. Afterwards, the script can be deleted.
3. Modify package dependencies and other settings in `pyproject.toml`.
4. Replace `src/.../main.py`, `tests/test_template.py`, and `docs/pages/api/main.md` with your package.

## Developing

See CONTRIBUTING.md for development instructions.