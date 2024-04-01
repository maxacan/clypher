import os
from clypher.file_handlers.file_handler import FileHandler
import pytest
from pathlib import Path

from rich.console import Console
CONSOLE = Console()


@pytest.fixture
def create_infile(tmp_path, name: str | None = None):
    if name is None:
        infile = tmp_path / "infile.txt"
    else:
        infile = tmp_path / name

    infile.write_text("this is a test")
    return infile


@pytest.fixture
def create_outfile(tmp_path, name: str | None = None):
    if name is None:
        outfile = tmp_path / "infile.txt.clypher"
    else:
        outfile = tmp_path / name

    outfile.write_text("This is encrypted")

    return outfile


@pytest.fixture
def create_file_pair(create_infile, create_outfile):
    return create_infile, create_outfile


class TestFileHandler:
    def test_fails_if_input_not_exists(self):

        with pytest.raises(FileNotFoundError):

            FileHandler(
                [Path("file.a")]
            )

    def test_fails_if_output_file_already_exists(self, create_file_pair):
        """
        The file handler should fail if an output file already exists and 
        --fo is false.
        """
        infile, _ = create_file_pair

        with pytest.raises(FileExistsError):
            FileHandler(
                [infile],
                force_overwrite=False
            )

    def test_request_single_file(self, create_infile):
        """
        Test if the file handler responds with a file when requested once.
        """
        infile = create_infile

        fh = FileHandler(
            files=[infile]
        )

        assert fh.request() == infile.read_bytes()

    def test_request_returns_none_if_no_more_files(self, create_infile):
        infile = create_infile

        fh = FileHandler(
            files=[infile]
        )

        fh.request()

        assert fh.request() is None

    def test_generates_correct_default_output_names_on_encryption(self, create_infile):
        """
        When encrypting, the file handler should add the .clypher extension to any files written.
        """

        infile = create_infile

        fh = FileHandler(
            files=[infile]
        )

        fh.request()
        fh.write(b"test")

        assert fh.output_filepath == Path(str(infile) + ".clypher")

    def test_generates_correct_default_output_names_on_decryption(self, tmp_path):
        """
        On decryption, the file handler should delete the .clypher extension.
        """
        infile = tmp_path / "encrypted.txt.clypher"
        infile.write_bytes(b"f91j2949s")

        fh = FileHandler(
            [infile],
            decrypting=True
        )

        fh.request()

        assert fh.output_filepath == tmp_path / "encrypted.txt"

    def test_writes_output_file_correctly(self, create_infile, tmp_path):
        """
        Test that an output is written when using FileHandler.write()
        """

        infile = create_infile

        fh = FileHandler(
            [infile]
        )

        fh.request()
        fh.write(b"encrypted test")

        assert (tmp_path / "infile.txt.clypher").is_file()

    def test_fails_when_output_dir_doesnt_exists(self, create_infile, tmp_path):
        """
        If the output directory specified by --out does not exist, the file handler should raise an error.

        ! Delete test if a directory creation function is added !

        """

        with pytest.raises(FileNotFoundError):
            FileHandler(
                files=[create_infile],
                output_dir=tmp_path / "non-existant-dir"
            )

    def test_places_files_in_output_dir(self, create_infile, tmp_path):
        """
        The FileHandler should correctly output files onto the directory specified by
        --out.
        """

        file1 = create_infile

        output_dir = tmp_path / "out"
        output_dir.mkdir()

        fh = FileHandler(
            files=[file1],
            output_dir=output_dir
        )

        fh.write(fh.request())

        assert Path.is_file(Path(output_dir / "infile.txt.clypher")), \
            f"The FileHandler failed to put an output file into the output directory."

    def test_fails_if_specified_output_is_a_file(self, create_file_pair):
        """
        The file handler should fail if --out refers to a file and not a directory.
        """
        infile, outfile = create_file_pair

        with pytest.raises(ValueError):
            FileHandler(
                files=[infile],
                output_dir=outfile,
                force_overwrite=False
            )

    def test_output_dir_is_input_parent(self, create_infile):
        """
        In previous versions, the program failed if the output directory was the same
        as the input file parent directory.

        The program should just place all the output files in the same directory.
        """

        infile = create_infile

        fh = FileHandler(
            files=[infile],
            output_dir=infile.parent
        )

        fh.write(fh.request())

        assert Path.is_file(Path(infile.parent / "infile.txt.clypher")), \
            "The FileHandler failed to save an output file to the input file parent directory."

    def test_file_gets_closed_after_request(self, create_infile):
        """
        When using the request() method of a File Handler, the read file should be closed
        once the request() function returns.
        """

        infile = create_infile

        fh = FileHandler(
            files = [infile]
        )

        read = fh.request()

        try:
            open(infile, "r")

        except IOError:
            self.fail("FileHandler.request() did not close the file after reading it.")
