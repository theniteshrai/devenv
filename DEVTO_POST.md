# Dev.to Article — Week 1 Launch

**Title**: I Built a Tool to Set Up Your Dev Environment in One Command

**Description**: Building DevEnv took me a weekend. Using it takes 10 seconds.

**Tags**: #python #golang #cli #developer-tools #opensource

**Body**:

## The Problem

Every time I get a new machine or reset my dev environment, I spend 2-4 hours running the same commands:
- Install Python tools (Black, Ruff, pytest, mypy)
- Install Go tools (golangci-lint, dlv, air)
- Configure shell (fzf, starship, aliases)
- Scaffold new projects with CI/CD, tests, linting

## The Solution: DevEnv

I built **DevEnv** — a CLI tool that does all of this with a single command.

```bash
pip install devenv
devenv init
```

That's it. Python and Go are configured. Shell tools are set up. New projects are scaffolded with CI/CD, tests, and linting.

## Features

- **Python setup**: Black, Ruff, pytest, mypy, pre-commit
- **Go setup**: golangci-lint, dlv (debugger), air (live reload)
- **Shell configuration**: fzf, starship prompt, aliases
- **Project scaffolding**: Generate new projects with everything included
- **Status dashboard**: Check what's installed and configured

## The Numbers

- **Before**: 2-4 hours of manual setup per machine
- **After**: 10 seconds
- **Time saved**: ~10 hours per year (if you switch machines 3x/year)

## Open Source

DevEnv is MIT licensed and open source. GitHub: https://github.com/theniteshrai/devenv

Would love contributions, issues, and feedback!

**Bonus**: I'm selling it on Gumroad for $9 with a "pay what you want" option. If you find it useful, consider supporting the project.

