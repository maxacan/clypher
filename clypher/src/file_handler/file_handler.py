import os
from pathlib import Path
from _version import __version__


class FileHandler:
    """
    Deals with file reading and writing, as well as with handling IOErrors and creating
    containers.
    """

    def __init__(
        self,
        files: list[Path],
        output_dir: Path | None = None,
        force_overwrite: bool = False,
        decrypting: bool = False
    ) -> None:

        for idx, path in enumerate(files):
            if path.is_dir():
                #FIXME Change this when support for directories is added
                raise NotImplementedError(
                    f"Clypher v {__version__} does not support encrypting directories yet.")
            if not path.is_file():
                raise FileNotFoundError(f"Cant find input file: {path}")
            
            # Convert to absolute
            files[idx] = os.path.abspath(path)

        if output_dir is not None:
            if output_dir.is_file():
                raise TypeError(
                    f"The output '{output_dir}' is a file, not a directory.")

            elif output_dir.is_dir():
               output_dir = os.path.abspath(output_dir)

            else:
                # If it is not a file nor an existing dir, then assume it to be a directory that
                # does not exist.
                raise FileNotFoundError(f"The output directory '{output_dir}' does not exist.")

                # if GUI.ask("Output directory doesnt exist, create it?"):
                #     mkdir()

        self.__out = output_dir
        self.__force_ow = force_overwrite
        self.__decrypting = decrypting
        self.__file_list = self._generate_file_list(files)

    def _exists(self, path: Path) -> bool:
        return path.is_file() or path.is_dir()

    def _generate_output_path(self, currfile: Path) -> Path:
        """
        Given a file path, generate and return its corresponding output file name.
        """

        # if --out is specified, then take that as the base output path
        # Otherwise, take the parent dir of each file.
        if self.__out is not None:
            base_output_path = self.__out
        else:
            base_output_path = currfile.parent

        if self.__decrypting:
            outfile = base_output_path / Path(currfile.name.rstrip(".clypher"))

        else:
            outfile = base_output_path / Path(currfile.name + ".clypher")

        return outfile

    def _generate_file_list(self, infiles: list[Path]) -> list[tuple[Path, Path]]:
        """
        Given a list of input file paths, generate and return a list of tuples of the form
        (input_filename, output_filename).
        """
        file_list = []

        # Remove possible duplicated files
        for file_ in set(infiles):
            file_ = Path(os.path.abspath(file_))

            output_path = self._generate_output_path(file_)

            if self._exists(output_path) and self.__force_ow is False:
                raise FileExistsError(
                    f"The output file for ({output_path}) for the input file ({file_}) already exists.")

            file_list.append((file_, output_path))

        return file_list

    def request(self) -> tuple[Path, bytes] | None:
        """
        Reads and returns the next file to be processed as bytes, along with its filename,
        or None if there are no more files to process.
        """
        try:
            self.currfile, self.output_filepath = self.__file_list.pop()
        
            with open(self.currfile, "rb") as f:
                return f.read()

        except IndexError:
            return None

    def write(self, data: bytes) -> int:
        """
        Write data to the file and return the number of bytes written.
        """
        with open(self.output_filepath, "wb") as f:
            return f.write(data)
