from clypher.src.file_handler.file_handler import FileHandler
import pytest
from pathlib import Path

from rich.console import Console
CONSOLE = Console()

@pytest.fixture
def create_infile(tmp_path):
    infile = tmp_path / "infile.txt"
    infile.write_text("this is a test")
    return infile

@pytest.fixture
def create_outfile(tmp_path):
    outfile = tmp_path / "infile.txt.clypher"
    outfile.write_text("This is encrypted")
    return outfile

@pytest.fixture 
def create_file_pair(create_infile, create_outfile):
    return create_infile, create_outfile

class TestFileHandler:
    def test_fh_fails_if_input_not_exists(self):

        with pytest.raises(FileNotFoundError):

            FileHandler(
                [Path("file.a")]
            )

    def test_fh_fails_if_specified_output_already_exists(self, create_file_pair):
        """
        The file handler should fail if --force-overwrite is false and an output
        file already exists.
        """
        infile, outfile = create_file_pair

        with pytest.raises(FileExistsError):
            FileHandler(
                files=[infile],
                out=outfile,
                force_overwrite=False
            )

    def test_fh_fails_if_automatic_output_already_exists(self, create_file_pair):
        infile, _ = create_file_pair

        with pytest.raises(FileExistsError):
            FileHandler(
                [infile],
                force_overwrite=False
            )

    def test_fh_request_single_file(self, create_infile):
        """
        Test if the file handler responds with a file when requested once.
        """
        infile = create_infile

        fh = FileHandler(
            files=[infile]
        )

        assert fh.request() == infile.read_bytes()

    def test_fh_request_returns_none_if_no_more_files(self, create_infile):
        infile = create_infile

        fh = FileHandler(
            files=[infile]
        )

        fh.request()

        assert fh.request() is None

    def test_fh_generates_correct_default_output_names_on_encryption(self, create_infile):
        """
        When encrypting, the file handler should add the .clypher extension to any files written.
        """

        infile = create_infile

        fh = FileHandler(
            files = [infile]
        )

        fh.request()
        fh.write(b"test")

        assert fh.output_filepath == Path(str(infile) + ".clypher")

    def test_fh_generates_correct_default_output_names_on_decryption(self, tmp_path):
        """
        On decryption, the file handler should delete the .clypher extension.
        """
        infile = tmp_path / "encrypted.txt.clyper"
        infile.write_bytes(b"f91j2949s")

        fh = FileHandler(
            [infile],
            decrypting=True
        )

        fh.request()

        assert fh.output_filepath == tmp_path / "encrypted.txt"

    def test_fh_fails_when_input_is_directory(self, tmp_path):
        """
        Make sure the base file handler fails if the input is a directory, as they are
        not supported yet.

        #TODO: Delete test when support for directories is added.
        """
        directory = tmp_path / "testdir"

        directory.mkdir()

        with pytest.raises(NotImplementedError):
            FileHandler(
                files = [directory]
            )

    def test_fh_writes_output_file_correctly_on_encryption(self, create_infile, tmp_path):
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

    def test_fh_fails_when_output_dir_not_exists(self, create_infile, tmp_path):
        """
        If the output directory specified by --out does not exist, the file handler should raise an error.

        #TODO: Remove if directory creation functionality is added.
        """

        with pytest.raises(FileNotFoundError):
            FileHandler(
                files = [create_infile],
                out = tmp_path / "non-existant-dir"
            )
