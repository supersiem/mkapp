import os
import typer


def main(
    command: str,
    url: str = typer.Argument(None, help="URL for cloning a project"),
    type: str = typer.Argument(None, help="Het type project"),
    name: str = typer.Argument(None, help="Project name"),
):
    if command == "make":
        if not name:
            typer.echo("Error: --name is required for 'make' command.")
            raise typer.Exit(code=1)
        if type == "js":
            os.system("mkdir " + name)
            os.system("cd " + name + " && npm init -y")
            os.system("git init")
        elif type == "python":
            os.system("mkdir " + name)
            os.system("cd " + name + " && python -m venv venv")
            os.system("git init")
        elif type == "cf":
            os.system("mkdir " + name)
            os.system("cd " + name)
            os.system("git init")
            os.system(
                "git submodule add https://github.com/supersiem/custom_framework.git"
            )
    elif command == "clone":
        if not url:
            typer.echo("Error: --url is required for 'clone' command.")
            raise typer.Exit(code=1)
        os.system("git clone " + url)


if __name__ == "__main__":
    typer.run(main)
