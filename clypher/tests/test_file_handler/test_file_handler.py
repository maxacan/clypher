from clypher.src.file_handler.file_handler import FileHandler
import pytest
from pathlib import Path


class TestFileHandler:
    def test_file_handler_fails_if_input_not_exists(self):

        with pytest.raises(FileNotFoundError):
            
            FileHandler(
                [Path("file.a")]
            )
