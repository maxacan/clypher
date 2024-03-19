from src.encryptors.base_encryptor import BaseEncryptor
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from os import urandom
from base64 import b64encode


class FernetEncryptor(BaseEncryptor):
    """
    Encrypt and decrypt files using Fernet.
    """

    def __init__(self, password: bytes) -> None:
        super().__init__(password)

    def __init_fernet(self, salt: bytes | None = None):

        if salt is None:
            self.__salt = urandom(16)
        else:
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
