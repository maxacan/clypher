import importlib
from ..engines import INSTALLED_ENGINES

def import_engine(engine:str, engine_list: dict = INSTALLED_ENGINES):
    """
    Given a string engine, return the engine class that it represents.

    Raise ImportError if the engine cannot be imported.
    """

    try:
        engine = engine_list[engine]
        module_name, class_name = engine.rsplit(".", 1)
        module = importlib.import_module(module_name)
        engine_class = getattr(module, class_name)

        return engine_class

    except AttributeError as e:
        raise e(f"The specified engine module {module_name} has no class {class_name}.")

    except (ImportError, KeyError):
        raise SystemExit(f"The engine {engine} does not exist. Are you sure it is installed?")

