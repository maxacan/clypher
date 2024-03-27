from src.encryptors.base_encryptor import BaseEncryptor
from src.logging_config.logger_config import get_logger_or_debug
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from os import urandom
from base64 import b64encode


LOG = get_logger_or_debug(__name__)

class FernetEncryptor(BaseEncryptor):
    """
    Encrypt and decrypt files using Fernet.
    """

    def __init__(self, password: bytes) -> None:
        LOG.debug(f"Initializing a FernetEncryptor instance.")
        super().__init__(password)

    def __init_fernet(self, salt: bytes | None = None):

        LOG.debug(f"Initializing Fernet.")

        if salt is None:
            self.__salt = urandom(16)
            LOG.debug(f"Created random salt.")

        else:
            LOG.debug("Using recovered salt.")
            self.__salt = salt

        self.__scrypt_instance = Scrypt(
            salt=self.__salt,
            length=32,
            n=2**18,
            r=8,
            p=1
        )

        self.__derived_password = b64encode(
            self.__scrypt_instance.derive(self.password))

        self.__fernet_instance = Fernet(self.__derived_password)

        LOG.debug("Fernet instance initialized.")

    def encrypt(self, data: bytes | bytearray) -> bytearray:
        self.__init_fernet()

        return bytearray(self.__salt) + bytearray(self.__fernet_instance.encrypt(data))

    def decrypt(self, data: bytes | bytearray) -> bytes:
        self.__init_fernet(salt=data[:16])

        return self.__fernet_instance.decrypt(
            bytes(
                data[len(self.__salt):]
            )
        )
