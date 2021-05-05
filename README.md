# Python CLI Template

A Python CLI application template, using pre-commit, black, flake8, pydocstyle
and mypy to enforce code quality.

## Getting started

Install requirements:

```Bash
pip install -r requirements.txt
```

Install the `pre-commit` hook environment:

```Bash
pre-commit install
```

## Code Style

Code style is checked by the pre-commit hook, according to `.pre-commit-config.yaml`,
as well as in the GitHub Actions workflow at `.github/workflows/style.yaml`.

Code style adheres to the default `black` format, which formats code to a
line length of 80+8 characters. `flake8` is set up to use `flake8-bugbear`,
which will tolerate lines up to 88 characters before failing, but will encourage
you to keep lines to 80 characters where possible.
