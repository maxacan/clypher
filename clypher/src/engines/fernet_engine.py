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
            output_dir=self.output,
            force_overwrite=self.force_ow,
            decrypting=decrypting
        )

    def start_encryption(self):
        print("\n[cyan]Starting encryption. [/cyan]")

        while (file_ := self.__fhandler.request()):
            # HACK: Print to the console directly for now.
            # Change this to use the GUI API when implemented.
            print(self.__fhandler.currfile, end="... ")
            
            self.__fhandler.write(
                self.__encryptor.encrypt(
                    file_
                )
            )
            print("[bold green] OK [/bold green]")

    def start_decryption(self):
        # HACK: Print to the console for now.
        print("\n[cyan]Starting decryption... [/cyan]")
        
        while (file_ := self.__fhandler.request()):
            
            print(self.__fhandler.currfile, end="... ")

            self.__fhandler.write(
                self.__encryptor.decrypt(
                    file_
                )
            )

            print("[bold green]OK[/bold green]")
