import pkg_resources
from os import path

from typer.testing import CliRunner
from clypher.main import app

runner = CliRunner()


def test_version():
    """
    Test that the version message is displayed correctly.
    """
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0, "Version command exited with non-zero exit code."
    assert "Clypher" in result.stdout
    assert pkg_resources.require(
        'clypher')[0].version in result.stdout, "No version number in version command."


def test_enc_fails_if_no_args_passed():
    """
    Test if the enc command fails if no arguments were passed.
    """

    result = runner.invoke(app, ["enc"])

    assert result.exc_info[0] is SystemExit, \
        "The enc command didn't exit when no input was provided."


def test_enc_fails_if_implicit_and_explicit_inputs():
    """
    Test if the enc command fails if the user specifies an implicit file name, followed by 
    the use of the --in option.
    """

    result = runner.invoke(app, ["enc", "infile", "--in", "secondinfile"])

    assert result.exc_info[0] is SystemExit, \
        "The enc command didn't exit when implicit and explicit inputs were provided."


def test_enc_fails_if_implicit_input_does_not_exist(tmp_path):

    fake_file = path.join(tmp_path, "infile.asd")

    result = runner.invoke(app, ["enc", fake_file])
    print(f"\n\n {result.exc_info}\n\n")

    assert result.exc_info[0] is FileNotFoundError, \
        "The enc command didn't fail when an implicit input was provided but didn't exist."


def test_enc_fails_if_explicit_input_does_not_exist(tmp_path):

    fake_file = path.join(tmp_path, "infile.asd")

    result = runner.invoke(app, ["enc", "--in", fake_file])
    print(f"\n\n {result.exc_info}\n\n")

    assert result.exc_info[0] is FileNotFoundError, \
        "The enc command didn't fail when an explicit input was provided but didn't exist."

# TODO: Que falle si queres usar más de un archivo en files y una sola --out
def test_enc_fails_if_multiple_in_single_out():
    """
    Test if the enc command fails if the user inputs multiple files with only one explicit output.
    """

    result = runner.invoke(app, ["enc", "file1.a", "file2.a", "--out", "file1.out"])

    assert result.exc_info[0] is SystemExit, \
        "The enc command didn't fail on multiple inputs with a single output."