# DevEnv

One-command dev environment setup for Python & Go developers.

🌐 **Website**: [devenv.live](https://devenv.live)
📦 **GitHub**: [theniteshrai/devenv](https://github.com/theniteshrai/devenv)
💰 **Buy**: [Gumroad](https://gumroad.com/devenv) — $9 (pay what you want)

## Quick Start

```bash
pip install devenv
devenv init
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

## Install

```bash
# From PyPI
pip install devenv

# From GitHub
git clone https://github.com/theniteshrai/devenv
cd devenv && pip install -e .

# Standalone (zero dependencies)
python3 devenv-standalone.py
```

## License

MIT
