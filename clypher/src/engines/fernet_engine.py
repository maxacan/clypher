from src.encryptors.fernet_encryptor import FernetEncryptor
from src.file_handler.file_handler import FileHandler
from .base_engine import BaseEngine
from rich import print


class FernetEngine(BaseEngine):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__encryptor = FernetEncryptor(
            password=self.password
        )

        self.__fhandler = FileHandler(
            files=self.infiles,
            out=self.output,
            force_overwrite=self.force_ow
        )

    def start_encryption(self):
        print("\n[cyan]Starting encryption. [/cyan]")
        while (file_ := self.__fhandler.request()):
            # TODO: enviar señal de inicio a la gui
            print(file_, end="... ")
            

            self.__fhandler.write(
                self.__encryptor.encrypt(
                    file_
                )
            )
            print("[bold green] OK [/bold green]")
            # TODO: Enviar señal de final a la gui

    def start_decryption(self):
        #TODO: Desencrypcion
        pass
