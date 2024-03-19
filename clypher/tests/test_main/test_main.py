import pkg_resources
from typer.testing import CliRunner

from clypher.__main__ import app
from clypher._version import __version__

RUNNER = CliRunner()


def test_version():
    """
    Test that the version message is displayed correctly.
    """
    result = RUNNER.invoke(app, ["version"])

    assert result.exit_code == 0, "Version command exited with non-zero exit code."
    assert "Clypher" in result.stdout
    assert __version__ in result.stdout, "No version number in version command."


def test_enc_fails_if_no_args_passed():
    """
    Test if the enc command fails if no arguments were passed.
    """

    result = RUNNER.invoke(app, ["enc"])

    assert result.exc_info[0] is SystemExit, \
        "The enc command didn't exit when no input was provided."


def test_enc_fails_if_implicit_and_explicit_inputs():
    """
    Test if the enc command fails if the user specifies an implicit file name, followed by 
    the use of the --in option.
    """

    result = RUNNER.invoke(app, ["enc", "infile", "--in", "secondinfile"])

    assert result.exc_info[0] is SystemExit, \
        "The enc command didn't exit when implicit and explicit inputs were provided."


def test_enc_fails_if_multiple_in_single_out():
    """
    Test if the enc command fails if the user inputs multiple files with only one explicit output.
    #TODO: Sacar esto, o dejarlo unicamente si la salida son archivos
    """

    result = RUNNER.invoke(
        app, ["enc", "file1.a", "file2.a", "--out", "file1.out"])

    assert result.exc_info[0] is SystemExit, \
        "The enc command didn't fail on multiple inputs with a single output."
