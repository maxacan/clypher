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
        out: Path | None = None,
        force_overwrite: bool = False,
        decrypting: bool = False
    ) -> None:

        for path in files:
            if path.is_dir():
                raise NotImplementedError(
                    f"Clypher v {__version__} does not support encrypting directories yet.")
            if not path.is_file():
                raise FileNotFoundError(f"Cant find file: {path}")

        if out is not None:
            # Que out sea solo para directorios. Si no existen o son archivos, tirar error
            if out.is_file():
                raise TypeError(
                    f"The output '{out}' is a file, not a directory.")

            elif out.is_dir():

                pass

            else:
                # If it is not a file nor an existing dir, then it must be a directory that
                # does not exist.
                raise FileNotFoundError(f"The output directory '{out}' does not exist.")
                #TODO: Intentar crearlo? Algo como:

                # if GUI.ask("Output directory doesnt exist, create it?"):
                #     mkdir()

        self.__out = out
        self.__force_ow = force_overwrite
        self.__decrypting = decrypting
        self.__file_list = self._generate_file_list(files)

    def _exists(self, path: Path) -> bool:
        return path.is_file() or path.is_dir()

    def _generate_output_path(self, currfile: Path) -> Path:
        """
        Given a file path, generate and return its corresponding output file name.
        """

        #TODO: Añadir soporte para poner todos los archivos en un directorio de salida.
        #TODO: Ver si se puede trabajar con paths absolutos porque 
        # parece que --out trabaja desde el directorio de la entrada.


        prefix = ""
        if self.__out:
            prefix = self.__out


        if self.__decrypting:
            outfile = currfile.parent / Path(prefix) /\
                Path(currfile.name.rstrip(".clypher"))

        else:
            outfile = currfile.parent / Path(prefix) / Path(currfile.name + ".clypher")

        return outfile

    def _generate_file_list(self, infiles: list[Path]) -> list[tuple[Path, Path]]:
        """
        Given a list of input file paths, generate and return a list of tuples of the form
        (input_filename, output_filename).
        """
        file_list = []
        for file_ in infiles:
            output_path = self._generate_output_path(file_)
            # TODO: mantener extension original del archivo al encriptar.
            # para que se pueda restaurar la extensión si por alguna razón
            # se la pierde. Capaz ponerla al inicio del archivo encriptado.
            # Esto requeriría cambiar como se guarda la sal.
            if output_path.is_dir():
                if self._exists(output_path / file_) and self.__force_ow is False:
                    raise FileExistsError(
                        f"The output file for ({output_path}) for the input file ({file_}) already exists.")

                file_list.append((file_, output_path / file_))

            else:
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

            # TODO: Dividir en chunks para no tener que cargar todo el archivo en memoria.

            return open(self.currfile, "rb").read()
        except IndexError:
            return None

    def write(self, data: bytes) -> None:
        # TODO: Si no existe el directorio, hay que crearlo
        with open(self.output_filepath, "wb") as f:
            f.write(data)
