"""
Clypher. Encrypt files from the command line.
Copyright (C) 2024 Maximiliano Cancelarich

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

For contacting me, send me an email at maximilianoacan@gmail.com.

Please be aware that THIS PROGRAM IS NOT INTENDED AS A CRYPTOGRAPHICALLY SECURE encryption solution.
"""

import sys
import logging
import typer

from typing import List, Optional
from pathlib import Path
from os import environ

from typing_extensions import Annotated

from _version import __version__
from src.import_handler.import_handler import import_engine
from src.cli.managers import ConsoleManager as CONSOLE

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


@app.command()
def version():
    """
    Prints the current package version.
    """
    CONSOLE.print_version_msg()


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
        CONSOLE.error("No input was provided.")
        raise SystemExit(1)

    if password is None:
        password = CONSOLE.ask_password(mode="decryption")

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
        CONSOLE.error("No input was provided.")
        raise SystemExit(1)

    if password is None:
        password = CONSOLE.ask_password(mode="encryption")

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
    CONSOLE.print_banner()
    app()


if __name__ == "__main__":

    main()
