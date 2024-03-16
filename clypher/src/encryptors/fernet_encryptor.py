from src.encryptors.base_encryptor import BaseEncryptor
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from os import urandom
from base64 import b64encode


class FernetEncryptor(BaseEncryptor):
    """
    Encrypt and decrypt files using Fernet.
    """

    def __init__(
        self,
        password: bytes,
        salt_length: int = 16
    ) -> None:

        super().__init__(password)

        self.__salt = urandom(salt_length)
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
        return bytearray(self.__salt) + bytearray(self.__fernet_instance.encrypt(data))

    def decrypt(self, data: bytes | bytearray) -> bytes:
        # This assumes that the salt length never changed between encryption and
        # decryption.
        return self.__fernet_instance.decrypt(
            bytes(
                data[len(self.__salt):]
            )
        )

