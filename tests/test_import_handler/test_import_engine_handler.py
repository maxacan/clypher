from import_handler.import_handler import import_engine
import pytest


def test_import_engine_fails_if_engine_doesnt_exist():
    engine_list = {"fake": "clypher.src.engines.fake.FakeEngine"}

    with pytest.raises(SystemExit):
        import_engine("also_fake", engine_list=engine_list)
