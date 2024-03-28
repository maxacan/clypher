from .messages import *
from _console import console, stderr_console
from rich.progress import (
    Progress,
    )

import typer

class ConsoleManager:
    """
    The class responsible for pretty printing in the console.
    """

    @staticmethod
    def print_version_msg():
        console.print(VERSIONMSG)

    @staticmethod
    def print_banner():
        console.print(BANNER)

    @staticmethod
    def error(msg: str, show_tag: bool = True, color_msg: bool = True):
        """
        Display a bold [ERROR] tag in red, followed by the message in msg, also in red.

        If show_tag is False, the [ERROR] tag will be skipped.

        If color_msg is False, only the tag will be red.
        """

        message = ""

        if show_tag:
            message += "[bold red]\[ERROR]: [/bold red]"

        if color_msg:
            message += f"[red]{msg}[/red]"
        else:
            message += msg

        stderr_console.print(message)

    @staticmethod
    def warn(msg: str, show_tag: bool = True, color_msg: bool = True):
        """
        Display a bold [WARNING] tag in red, followed by the message in msg, also in red.

        If show_tag is False, the [WARNING] tag will be skipped.

        If color_msg is False, only the tag will be red.
        """

        message = ""

        if show_tag:
            message += "[bold red]\[WARNING]: [/bold red]"

        if color_msg:
            message += f"[red]{msg}[/red]"
        else:
            message += msg

        console.print(message)

    @staticmethod
    def info(msg: str, show_tag: bool = True):
        """
        Display a bold [INFO] tag in blue, followed by msg.

        If show_tag is false, don't show [INFO]
        """

        message = ""

        if show_tag:
            message += "[bold bright_blue]\[INFO]: [/bold bright_blue]"

        message += msg

        console.print(message)

    @staticmethod
    def success(msg: str, show_tag: bool = True):
        """
        Display a bold [SUCCESS] tag in green, followed by msg.

        If show_tag is false, don't show [SUCCESS]
        """

        message = ""

        if show_tag:
            message += "[bold bright_green]\[SUCCESS]: [/bold bright_green]"

        message += msg

        console.print(message)

    @staticmethod
    def ask_password(mode: str = "encryption") -> str:
        """
        Prompt the user for a password, depending on `mode`.

        Return the plaintext password.
        """

        if mode == "encryption":
            ConsoleManager.warn("Choose a password carefully.")
            console.print(
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
        
        else:
            raise ValueError(f"The mode '{mode}' is not recognized as a valid mode for prompting a password.")

    @staticmethod
    def prompt(msg: str, *args, **kwargs) -> str:
        return typer.prompt(text=msg, *args, **kwargs)
    
    @staticmethod
    def confirm(msg: str, *args, **kwargs) -> str:
        return typer.confirm(text=msg, *args, **kwargs)

class ProgressManager:
    def __init__(self, msg: str, total: int, *args, **kwargs) -> None:
        self.progress = Progress(*args, **kwargs)
        self._task = self.progress.add_task(msg, total=total)

    def step(self, msg: str | None = None) -> None:
        """
        Update the current task.
        If msg is a string, update the task description every time a step is performed.
        """

        if msg is not None:
            self.progress.print(msg)

        self.progress.update(self._task, advance=1)