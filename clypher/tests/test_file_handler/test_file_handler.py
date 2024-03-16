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
        infile, outfile = create_file_pair


        with pytest.raises(FileExistsError):
            fh = FileHandler(
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

    def test_fh_generates_correct_default_output_names(self, create_infile):
        """
        Test if the file handler can correctly generate output names.
        """

        infile = create_infile

        fh = FileHandler(
            files = [infile]
        )

        fh.request()
        fh.write(b"test")

        assert fh.__dict__["_FileHandler__output_filepath"] == Path(str(infile) + ".clypher")

    def test_fh_writes_output_file_correctly(self, create_infile, tmp_path):
        
        infile = create_infile

        fh = FileHandler(
            [infile]
        )

        fh.request()
        fh.write(b"encrypted test")

        assert (tmp_path / "infile.txt.clypher").is_file()

