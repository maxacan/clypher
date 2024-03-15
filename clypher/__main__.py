import pkg_resources

import typer

from typing import List, Optional
from pathlib import Path

from typing_extensions import Annotated
from rich import print
from rich.align import Align


from src.file_handler.file_handler import FileHandler

app = typer.Typer(
    pretty_exceptions_show_locals=False
)

VERSIONNO = pkg_resources.require('clypher')[0].version
VERSIONMSG = f"[bold blue]Clypher[/bold blue] v{VERSIONNO}"

BANNER = Align(
    f"""[bold cyan]
   ___ _             _               
  / __\ |_   _ _ __ | |__   ___ _ __ 
 / /  | | | | | '_ \| '_ \ / _ \ '__|
/ /___| | |_| | |_) | | | |  __/ |   
\____/|_|\__, | .__/|_| |_|\___|_|   
         |___/|_| v{VERSIONNO}

[/bold cyan]""", align="center")


@app.command()
def version():
    """
    Prints the current package version.
    """
    print(VERSIONMSG)


@app.command()
def enc(
    input_files: Annotated[
        List[Path],
        typer.Argument()
    ] = None,
    _in: Annotated[
        Optional[Path],
        typer.Option(
            "--in",
            help="Input file or directory.")
    ] = None,
    out: Annotated[
        Optional[Path],
        typer.Option(help="Output file name.")
    ] = None,
    password: Annotated[
        Optional[str],
        typer.Option(
            "--pass",
            help="Pass the password as an option.")
    ] = None,
    force_overwrite: Annotated[
        bool,
        typer.Option(
            "--fo",
            help="If used, force the app to overwrite any output files that may already exist. Defaults to False."
        )
    ] = False
):
    """
    Encrypt the file, files or directories passed as arguments.
    """
    if len(input_files) == 0 and _in is None:
        raise SystemExit("ERROR: No input was provided.")

    if input_files:
        # Remove duplicates
        input_files = set(input_files)

        # Check if both input methods aren't being used at the same time.
        if _in:
            raise SystemExit(
                (
                    f"Specified a standalone filename {[str(x) for x in input_files]} along with using [--in {_in}].\n"
                    f"Choose one or the other."
                )
            )

        # Check if there are multiple inputs and a single output. If so, fail
        if len(input_files) > 1 and out is not None:
            # TODO: Añadir mensaje que explique qué pasó
            raise SystemExit(
                "ERROR: Multiple inputs mapped to a single output.")


    fa = FileHandler(
        files=input_files or _in,
        out = out,
        force_overwrite=force_overwrite
    )

    if not password:
        print("[bold red]WARNING:[/bold red] Choose a password carefully.")
        print(
            "Once encrypted, [bold red] the file CANNOT be restored unless the correct password is provided.[/bold red]")

        password = typer.prompt(
            text="Enter a password to be used for the file encryption",
            hide_input=True,
            confirmation_prompt=True
        )


def main():
    print(BANNER)
    app()

if __name__ == "__main__":
    main()
