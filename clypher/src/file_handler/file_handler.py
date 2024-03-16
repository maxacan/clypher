from pathlib import Path

#TODO añadir soporte para directorios
# no debería ser más que modificar esta clase. Total la encrypcion es la misma
#TODO: Mover a una clase abstracta, y tener dos clases distintas, una para directorio y otra para archivos
# después, crear un adaptador para los dos, que se maneje solo con el encryptor y los handlers

class FileHandler:
    """
    Deals with file reading and writing, as well as with handling IOErrors and creating
    containers.
    """

    def __init__(
        self,
        files: list[Path],
        out: Path | None = None,
        force_overwrite: bool = False
    ) -> None:

        for path in files:
            if not (path.is_file() or path.is_dir()):
                raise FileNotFoundError(f"Cant find file or directory: {path}")

        if out is not None:
            if out.is_file():
                if force_overwrite:
                    # TODO: levantar una warning o algo.
                    pass
                else:
                    raise FileExistsError(
                        f"The output file {out} already exists.")

        self.__out = out
        self.__force_ow = force_overwrite
        self.__file_list = self._generate_file_list(files)

    def _exists(self, path: Path) -> bool:
        return path.is_file() or path.is_dir()

    def _generate_output_path(self, currfile: Path) -> Path:
        """
        Given a file path, generate and return its corresponding output file name.
        """
        if self.__out:
            outfile = self.__out
        else:
            outfile = currfile.parent / \
                Path(currfile.name + ".clypher")

        return outfile

    def _generate_file_list(self, infiles: list[Path]) -> list[tuple[Path, Path]]:
        """
        Given a list of input file paths, generate and return a list of tuples of the form
        (input_filename, output_filename).
        """
        file_list = []
        for file_ in infiles:
            output_path = self._generate_output_path(file_)

            if self._exists(output_path) and self.__force_ow is False:
                raise FileExistsError(
                    f"The output file for ({output_path}) for the input file ({file_}) already exists.")
            
            file_list.append((file_, output_path))

        return file_list

    def request(self) -> bytes | None:
        """
        Reads and returns the next file to be encrypted as bytes, or None if there are no more files
        to encrypt.
        """
        try:
            self.__currfile, self.__output_filepath = self.__file_list.pop()

            # TODO: Dividir en chunks para no tener que cargar todo el archivo en memoria.

            return open(self.__currfile, "rb").read()
        except IndexError:
            return None

    def write(self, data: bytes) -> None:
        #TODO: Si no existe el directorio, hay que crearlo
        with open(self.__output_filepath, "wb") as f:
            f.write(data)
