from pathlib import Path


class FileHandler:
    """
    Deals with file reading and writing, as well as with handling IOErrors and creating
    containers.
    """

    def __init__(
        self,
        files: list[Path] | None = None,
        out: Path | None = None,
        force_overwrite: bool = False
    ) -> None:
        
        for path in files:
            if not (path.is_file() or path.is_dir()):
                raise FileNotFoundError(f"Cant find file or directory: {path}")
