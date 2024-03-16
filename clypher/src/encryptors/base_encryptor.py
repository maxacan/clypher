from abc import ABC,  abstractmethod

class BaseEncryptor(ABC):
    """
    Provides a common interface for creating concrete encryptor classes.
    """

    def __init__(self, password: bytes) -> None:
        self.password = bytes(password, encoding="utf-8")
    
    @abstractmethod
    def encrypt(self, data: bytes) -> bytes:
        pass

    @abstractmethod
    def decrypt(self, data: bytes) -> bytes:
        pass