from clypher.engines.fernet_engine import FernetEngine
from os.path import exists

def test_empty_file(tmp_path):
    """
    If an engine reads an empty file, it should skip it, instead of 
    stopping the file processing.
    """

    empty_file = tmp_path / "empty.txt"
    test_file = tmp_path / "test.txt"
    
    #Create empty file
    open(empty_file, "a").close()

    test_file.write_text("testtesttest")

    engine = FernetEngine(
        infiles = [empty_file, test_file],
        output = None,
        force_ow = False,
        password = "1234",
        recursive = False
    )

    engine.start_encryption()

    assert not exists(tmp_path / "empty.txt.clypher")
    assert exists(tmp_path / "test.txt.clypher")
