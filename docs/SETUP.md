# Requirements and Setup

- [Requirements and Setup](#requirements-and-setup)
    * [Requirements](#requirements)
    * [Setup](#setup)
        + [pipenv](#pipenv)
        + [npm](#npm)
        + [pre-commit](#pre-commit)

## Requirements

| Tool                                                                                     | Description                                     |
|:-----------------------------------------------------------------------------------------|:------------------------------------------------|
| [Pipenv](https://pypi.org/project/pipenv/)                                               | Required by AWS CDK, AWS CLI and pre-commit     |
| [pre-commit](https://pre-commit.com/)                                                    | Used to ensure standard prior to commits        |

## Setup

### pipenv

Pipenv is used to manage all python dependencies.

```shell
pip install pipenv
```

```shell
pipenv install -d
```

```shell
pipenv shell
```

### pre-commit

[pre-commit](https://pre-commit.com/) is used to enforce standards on this repository prior to committing any changes. This forms part of
our [Contributing](../CONTRIBUTING.md) standards. Please also see the
[pre-commit-config.yaml](../.pre-commit-config.yaml) file.

This is installed via the Pipfile, though this has to be initialised within this repository by running the below
command:

```shell
pre-commit install
```
