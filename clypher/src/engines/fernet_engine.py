from src.encryptors.fernet_encryptor import FernetEncryptor
from src.logging_config.logger_config import get_logger_or_debug
from src.file_handlers.file_handler import FileHandler
from .base_engine import BaseEngine
from rich import print

LOG = get_logger_or_debug(__name__)

class FernetEngine(BaseEngine):
    def __init__(self, decrypting: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__encryptor = FernetEncryptor(
            password=self.password
        )
        #TODO: pass args and kwargs for modifing kdf parameters.

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
            
            LOG.info(f"Encrypting file {self.__fhandler.currfile}...")

            self.__fhandler.write(
                self.__encryptor.encrypt(
                    file_
                )
            )

            LOG.info(f"Done")

            print("[bold green] OK [/bold green]")

    def start_decryption(self):
        # HACK: Print to the console for now.
        print("\n[cyan]Starting decryption... [/cyan]")
        
        while (file_ := self.__fhandler.request()):
            
            print(self.__fhandler.currfile, end="... ")

            LOG.info(f"Decrypting file {self.__fhandler.currfile}...")

            self.__fhandler.write(
                self.__encryptor.decrypt(
                    file_
                )
            )

            LOG.info(f"Done.")

            print("[bold green]OK[/bold green]")
