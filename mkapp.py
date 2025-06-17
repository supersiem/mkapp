import os
import typer


def main(
    command: str,
    url: str = typer.Option(None, help="URL for cloning a project"),
    type: str = typer.Option(None, help="Het type project"),
    name: str = typer.Option(None, help="Project name"),
    vscode: bool = typer.Option(
        False, help="Open the project in VS Code after creation"
    ),
):
    if command == "make":
        os.chdir(os.path.expanduser("~/Documents"))
        if not name:
            typer.echo("Error: --name is required for 'make' command.")
            raise typer.Exit(code=1)
        if type == "js":
            os.system("mkdir " + name)
            os.chdir(name)
            os.system("npm init -y")
            os.system("git init")
        elif type == "ts":
            os.system("mkdir " + name)
            os.chdir(name)
            os.system("npm init -y")
            os.system("npm install typescript --save-dev")
            os.system("npx tsc --init")
            os.system("git init")
        elif type == "python":
            os.system("mkdir " + name)
            os.chdir(name)
            os.system("python -m venv venv")
            os.system("git init")
        elif type == "cf":
            os.system("mkdir " + name)
            os.chdir(name)
            os.system("git init")
            os.system(
                "git submodule add https://github.com/supersiem/custom_framework.git"
            )
        if vscode:
            os.system("code .")
    elif command == "clone":
        os.chdir(os.path.expanduser("~/Documents"))
        if not url:
            typer.echo("Error: --url is required for 'clone' command.")
            raise typer.Exit(code=1)
        os.system("git clone " + url)
    elif command == "commit":
        os.system(f"git add . && git commit -m '{name}' && git push")


# voer uit als het script direct wordt uitgevoerd
# (niet als het wordt geïmporteerd als module)
if __name__ == "__main__":
    typer.run(main)
