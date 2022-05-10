from abc import ABC, abstractmethod
from typing import Tuple
from linter.severity import Severity


class Rule(ABC):
    @staticmethod
    @abstractmethod
    def default_severity() -> str:
        pass

    @staticmethod
    @abstractmethod
    def applies_to() -> Tuple[str, ...]:
        pass

    def __init__(self, severity: Severity) -> None:
        self.severity = severity

    @abstractmethod
    def run(self, lookml) -> bool:
        pass
