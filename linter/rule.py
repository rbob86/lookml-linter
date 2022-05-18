from abc import ABC, abstractmethod
from typing import Tuple, Union
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

    def __init__(self, severity: Union[Severity, None] = None) -> None:
        if severity is not None:
            self.severity = severity

    @abstractmethod
    def run(self, lookml, user_attribute=None, search_terms=None) -> bool:
        pass
