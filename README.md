# DevEnv

One-command dev environment setup for Python & Go developers.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Install

```bash
pip install devenv
```

## Quick Start

```bash
# Set up your entire dev environment
devenv init

# Create a new project
devenv new my-app

# Check your environment status
devenv status
```

## Features

- **One-command setup** — Python, Go, shell configured in seconds
- **Project scaffolding** — Generate project templates with CI/CD, tests, linting
- **Status dashboard** — See what's installed and configured
- **Opinionated defaults** — Battle-tested configurations out of the box

## What's included

### Python
- Black, Ruff, pytest, mypy, pre-commit
- Virtual environment setup
- Dependency management

### Go
- golangci-lint, dlv (debugger), air (live reload)
- Module management
- Testing framework

### Shell
- fzf fuzzy finder
- Starship prompt configuration
- Useful aliases and functions

## License

MIT
