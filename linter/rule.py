from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, List, Tuple, TypedDict, Union

from linter.helpers import pascal_case_to_snake_case


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
    def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
        pass

    def message(self) -> str:
        return pascal_case_to_snake_case(self.__class__.__name__).replace('_', ' ').capitalize()
