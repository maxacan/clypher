from abc import ABC, abstractmethod
from pathlib import Path


class BaseEngine(ABC):

    def __init__(
        self,
        password: str,
        infiles: list[Path],
        output: Path,
        force_ow: bool
    ) -> None:
        self.password = password
        self.infiles = infiles
        self.output = output
        self.force_ow = force_ow

    @abstractmethod
    def start_encryption(self):
        pass

    @abstractmethod
    def start_decryption(self):
        pass
