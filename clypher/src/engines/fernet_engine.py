from src.encryptors.fernet_encryptor import FernetEncryptor
from src.logging_config.logger_config import get_logger_or_debug
from src.file_handlers.file_handler import FileHandler
from src.cli.managers import ConsoleManager as CONSOLE
from src.cli.managers import ProgressManager as PM
from .base_engine import BaseEngine

from cryptography.exceptions import InvalidSignature
from cryptography.fernet import InvalidToken

LOG = get_logger_or_debug(__name__)


class FernetEngine(BaseEngine):
    def __init__(self, decrypting: bool = False, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.__encryptor = FernetEncryptor(
            password=self.plaintext_password,
        )

        self.__fhandler = FileHandler(
            files=self.infiles,
            output_dir=self.output,
            force_overwrite=self.force_ow,
            decrypting=decrypting
        )

    def start_encryption(self):
        CONSOLE.info(f"Starting encryption. {self.__fhandler.file_ammount} files to encrypt.\n")
        files_processed = 0

        progress_indicator = PM(
            "[cyan]Encrypting...[/cyan]",
            self.__fhandler.file_ammount
        )

        try:
            with progress_indicator.progress:

                while (file_ := self.__fhandler.request()):
                    progress_indicator.step(self.__fhandler.currfile)


                    LOG.info(f"Encrypting file {self.__fhandler.currfile}...")

                    self.__fhandler.write(
                        self.__encryptor.encrypt(
                            file_
                        )
                    )

                    files_processed += 1

                    LOG.info(f"Done")

        except KeyboardInterrupt:
            CONSOLE.warn(f"Stopped encryption after {files_processed} files.\n")

        if files_processed > 0:
            CONSOLE.success(f"Successfully encrypted {files_processed} files.\n")

    def start_decryption(self):
        CONSOLE.info(f"Starting decryption. {self.__fhandler.file_ammount} files to decrypt.\n")
        files_processed = 0

        progress_indicator = PM(
            "[cyan]Dencrypting...[/cyan]",
            self.__fhandler.file_ammount
        )

        with progress_indicator.progress:
            while (file_ := self.__fhandler.request()):
                try:
                    progress_indicator.step(self.__fhandler.currfile)

                    LOG.info(f"Decrypting file {self.__fhandler.currfile}...")

                    self.__fhandler.write(
                        self.__encryptor.decrypt(
                            file_
                        )
                    )

                    files_processed += 1

                    LOG.info(f"Done.")
                except KeyboardInterrupt:
                    CONSOLE.warn(f"Stopped decryption after {files_processed} files.")

                except (InvalidSignature, InvalidToken):
                    progress_indicator.progress.stop()
                    CONSOLE.error(
                        (
                         "The specified file doesn't appear to have been encrypted with the Fernet engine,"
                         " or the specified password is incorrect."
                        )
                    )

        if files_processed > 0:
            CONSOLE.success(f"Successfully decrypted {files_processed} files.")
