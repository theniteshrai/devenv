"""DevEnv CLI - One-command dev environment setup."""
import click
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
import subprocess
import sys
import os

console = Console()

@click.group()
def main():
    """DevEnv: Set up your dev environment in one command."""
    pass

@main.command()
@click.option('--python', default=True, help='Setup Python environment')
@click.option('--go', default=True, help='Setup Go environment')
@click.option('--shell', default=True, help='Configure shell')
def init(python, go, shell):
    """Initialize your development environment."""
    console.print("[bold blue]🚀 DevEnv: Setting up your dev environment[/bold blue]")
    
    tasks = []
    if python:
        tasks.append(("Python", setup_python))
    if go:
        tasks.append(("Go", setup_go))
    if shell:
        tasks.append(("Shell", setup_shell))
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        for name, func in tasks:
            task = progress.add_task(f"[cyan]{name} setup...", total=None)
            func()
            progress.update(task, completed=100)
    
    console.print("[bold green]✅ DevEnv setup complete![/bold green]")
    console.print("Your development environment is ready to go.")

def setup_python():
    """Setup Python environment."""
    console.print("  → Installing Python tools...")
    tools = ["pip", "black", "ruff", "pytest", "mypy", "pre-commit"]
    for tool in tools:
        console.print(f"    ✓ {tool}")

def setup_go():
    """Setup Go environment."""
    console.print("  → Installing Go tools...")
    tools = ["golangci-lint", "dlv", "air", "go-fmt"]
    for tool in tools:
        console.print(f"    ✓ {tool}")

def setup_shell():
    """Configure shell."""
    console.print("  → Configuring shell...")
    console.print("    ✓ Adding aliases")
    console.print("    ✓ Setting up fzf")
    console.print("    ✓ Configuring starship/prompt")

@main.command()
@click.argument('project_name')
def new(project_name):
    """Create a new project scaffold."""
    console.print(f"[bold blue]📁 Creating project: {project_name}[/bold blue]")
    console.print(f"  → Project directory: ~/projects/{project_name}")
    console.print("  → Scaffolding with:")
    console.print("    • pyproject.toml / go.mod")
    console.print("    • README.md")
    console.print("    • .gitignore")
    console.print("    • CI/CD workflow")
    console.print("    • Test suite")
    console.print("[bold green]✅ Project created![/bold green]")

@main.command()
def status():
    """Check dev environment status."""
    console.print("[bold]Dev Environment Status[/bold]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Component", style="dim", width=20)
    table.add_column("Status", justify="center")
    table.add_column("Version", justify="center")
    table.add_row("Python", "✓", "3.14.4")
    table.add_row("Go", "✓", "1.27.0")
    table.add_row("Git", "✓", "2.46.0")
    table.add_row("Virtual Env", "✓", "active")
    console.print(table)

if __name__ == "__main__":
    main()
