
import sys
import logging
import typer

from typing import List, Optional
from pathlib import Path
from os import environ

from typing_extensions import Annotated
from rich import print
from rich.align import Align

from _version import __version__
from src.import_handler.import_handler import import_engine

debug = environ.get("CLYPHER_DEBUG", False)

if debug is False:
    sys.tracebacklimit = 0
    LOG = logging.getLogger(__name__)

else:
    sys.tracebacklimit = -1
    LOG = logging.getLogger("debug")


app = typer.Typer(
    pretty_exceptions_enable=environ.get(
        "CLYPHER_DEBUG", "false").lower() in ("true", "1")
)

#TODO: Move all of this to the GUI class one implemented ----------------------------
VERSIONMSG = f"[bold blue]Clypher[/bold blue] v{__version__}"

BANNER = Align(
    f"""[bold cyan]
   ___ _             _               
  / __\ |_   _ _ __ | |__   ___ _ __ 
 / /  | | | | | '_ \| '_ \ / _ \ '__|
/ /___| | |_| | |_) | | | |  __/ |   
\____/|_|\__, | .__/|_| |_|\___|_|   
         |___/|_| v{__version__}

[/bold cyan]""", align="center")


def ask_password(mode: str = "encryption"):

    #FIXME: This should be moved to the GUI class once implemented.

    if mode == "encryption":
        print("[bold red]WARNING:[/bold red] Choose a password carefully.")
        print(
            "Once encrypted, [bold red] the file CANNOT be restored unless the correct password is provided.[/bold red]")

        return typer.prompt(
            text="Enter a password to be used for the file encryption",
            hide_input=True,
            confirmation_prompt=True)
    
    elif mode == "decryption":
        return typer.prompt(
            text="Enter the file password",
            hide_input=True,
            )


@app.command()
def version():
    """
    Prints the current package version.
    """
    print(VERSIONMSG)


@app.command()
def dec(
    input_files: Annotated[
        List[Path],
        typer.Argument()
    ] = None,
    out: Annotated[
        Optional[Path],
        typer.Option(help="Output directory name.")
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
    ] = False,
    engine: Annotated[
        Optional[str],
        typer.Option(help="The encryption engine to use.")
    ] = "fernet"
):
    
    if len(input_files) == 0:
        raise SystemExit("ERROR: No input was provided.")

    if password is None:
        password = ask_password(mode="decryption")

    engine_class = import_engine(engine)

    engine_instance = engine_class(
        password=password,
        infiles=input_files,
        output=out,
        force_ow=force_overwrite,
        decrypting = True
    )

    engine_instance.start_decryption()


@app.command()
def enc(
    input_files: Annotated[
        List[Path],
        typer.Argument()
    ] = None,
    out: Annotated[
        Optional[Path],
        typer.Option(help="Output dir.")
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
    ] = False,
    engine: Annotated[
        Optional[str],
        typer.Option(help="The encryption engine to use.")
    ] = "fernet"
):
    """
    Encrypt the file, files or directories passed as arguments.
    """

    if len(input_files) == 0:
        raise SystemExit("ERROR: No input was provided.")

    if password is None:
        password = ask_password()

    # Import the engine needed for operation
    engine_class = import_engine(engine)

    engine_class = engine_class(
        password=password,
        infiles=input_files,
        output=out,
        force_ow=force_overwrite
    )

    engine_class.start_encryption()


def main():
    print(BANNER)
    app()


# FIXME If called as a package, the app crashes on startup.
if __name__ == "__main__":

    main()
