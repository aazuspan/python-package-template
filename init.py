from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from packaging.version import InvalidVersion, parse

WHITESPACE = [" ", "\t", "\n"]
# Valid PyPI identifier according to PEP 508
VALID_PACKAGE_NAME = r"^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$"


@dataclass
class PackageInfo:
    name: str
    description: str
    author: str
    github_user: str
    min_python: str

    @staticmethod
    def get_package_name() -> str:
        """Get a valid package name from the user."""
        package_name = input("Enter package name: ").strip()

        if not re.match(VALID_PACKAGE_NAME, package_name, flags=re.IGNORECASE):
            print("Invalid package name (see https://peps.python.org/pep-0508/#names).")
            return PackageInfo.get_package_name()

        return package_name

    @staticmethod
    def get_min_python(default: str = "3.10") -> str:
        """Get a valid minimum Python version from the user."""
        min_python = input(f"Enter minimum python version [{default}]: ") or default

        try:
            parse(min_python)
            return min_python
        except InvalidVersion:
            print("Python version could not be parsed.")
            return PackageInfo.get_min_python()

    @staticmethod
    def get_github_user() -> str:
        """Get a valid github username from the user."""
        github_user = input("Enter Github username: ").strip()

        if not github_user or any([char in github_user for char in WHITESPACE]):
            print("Github username must not be blank or contain whitespace.")
            return PackageInfo.get_github_user()

        return github_user

    @staticmethod
    def get_author() -> str:
        """Get a valid author name from the user."""
        author = input("Enter author name: ").strip()

        if not author:
            print("Author name must not be blank.")
            return PackageInfo.get_author()

        return author

    @staticmethod
    def get():
        name = PackageInfo.get_package_name()
        author = PackageInfo.get_author()
        github_user = PackageInfo.get_github_user()
        description = input("Enter package description (or leave empty): ")
        min_python = PackageInfo.get_min_python()

        return PackageInfo(
            name=name,
            description=description,
            author=author,
            github_user=github_user,
            min_python=min_python,
        )


def _replace_placeholder_strings(files: list[Path], placeholder: str, replacement: str):
    """Replace a placeholder string in a list of files."""
    print(f"Replacing '{placeholder}' with '{replacement}'...")

    for file in files:
        with open(file) as src:
            content = src.read()

        if placeholder not in content:
            raise ValueError(f"{placeholder} was not found in {file}!")

        new_content = content.replace(placeholder, replacement)

        with open(file, "w") as dst:
            dst.write(new_content)


def set_package_name(package_name: str):
    files = [
        "pyproject.toml",
        "README.md",
        "docs/mkdocs.yml",
        "docs/pages/api/main.md",
        "tests/test_template.py",
    ]

    _replace_placeholder_strings(
        [Path(f) for f in files],
        placeholder="PACKAGE_NAME",
        replacement=package_name,
    )

    Path("src/PACKAGE_NAME").rename(f"src/{package_name}")


def set_author_name(author: str):
    files = [
        "pyproject.toml",
        "LICENSE",
    ]

    _replace_placeholder_strings(
        [Path(f) for f in files],
        placeholder="AUTHOR_NAME",
        replacement=author,
    )


def set_github_username(username: str):
    files = [
        "pyproject.toml",
        "README.md",
        "docs/mkdocs.yml",
    ]

    _replace_placeholder_strings(
        [Path(f) for f in files],
        placeholder="GITHUB_USERNAME",
        replacement=username,
    )


def set_description(description: str):
    if not description:
        return

    _replace_placeholder_strings(
        [Path("pyproject.toml")],
        placeholder="PACKAGE_DESCRIPTION",
        replacement=description,
    )


def set_min_python(min_python: str):
    _replace_placeholder_strings(
        [Path("pyproject.toml")],
        placeholder="3.9",
        replacement=min_python,
    )

    python_versions = ["3.7", "3.8", "3.9", "3.10", "3.11", "3.12"]
    # Format a list of supported python versions, e.g. "'3.10', '3.11', '3.12'"
    supported_python = str(python_versions[python_versions.index(min_python) :])[1:-1]

    _replace_placeholder_strings(
        [Path(".github/workflows/ci.yaml")],
        placeholder="PYTHON_VERSIONS",
        replacement=supported_python,
    )


if __name__ == "__main__":
    package_info = PackageInfo.get()

    set_package_name(package_info.name)
    set_author_name(package_info.author)
    set_github_username(package_info.github_user)
    set_description(package_info.description)
    set_min_python(package_info.min_python)

    if input("Delete this script? [y/N]").lower() == "y":
        Path("./init.py").unlink()
