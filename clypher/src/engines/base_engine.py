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
        raise NotImplementedError(f"Classes subclassing BaseEngine must define a start_encryption method.")

    @abstractmethod
    def start_decryption(self):
        raise NotImplementedError(f"Classes subclassing BaseEngine must define a start_decryption method.")
