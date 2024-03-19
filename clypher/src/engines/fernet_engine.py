from src.encryptors.fernet_encryptor import FernetEncryptor
from src.file_handler.file_handler import FileHandler
from .base_engine import BaseEngine
from rich import print


class FernetEngine(BaseEngine):
    def __init__(self, decrypting: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__encryptor = FernetEncryptor(
            password=self.password
        )

        self.__fhandler = FileHandler(
            files=self.infiles,
            out=self.output,
            force_overwrite=self.force_ow,
            decrypting=decrypting
        )

    def start_encryption(self):
        print("\n[cyan]Starting encryption. [/cyan]")

        while (file_ := self.__fhandler.request()):
            # TODO: enviar señal de inicio a la gui
            print(self.__fhandler.currfile, end="... ")
            
            self.__fhandler.write(
                self.__encryptor.encrypt(
                    file_
                )
            )
            print("[bold green] OK [/bold green]")
            # TODO: Enviar señal de final a la gui

    def start_decryption(self):
        print("\n[cyan]Starting decryption... [/cyan]")
        
        while (file_ := self.__fhandler.request()):
            
            print(self.__fhandler.currfile, end="... ")

            self.__fhandler.write(
                self.__encryptor.decrypt(
                    file_
                )
            )

            print("[bold green]OK[/bold green]")
