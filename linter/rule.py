from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Tuple, TypedDict, Union


class Severity(Enum):
    ERROR = 'error'
    WARNING = 'warning'
    IGNORE = 'ignore'


class ParamSet(TypedDict):
    user_attribute: str
    search_terms: List[str]


class Rule(ABC):
    @staticmethod
    @abstractmethod
    def applies_to() -> Tuple[str, ...]:
        pass

    def __init__(self, severity: Severity, params: Union[ParamSet, None] = None) -> None:
        self.severity = severity
        self.params = params

    @abstractmethod
    def run(self, lookml_object) -> bool:
        pass
