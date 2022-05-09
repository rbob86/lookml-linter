from abc import ABC, abstractmethod
from linter.severity import Severity


class Rule(ABC):
    @staticmethod
    @abstractmethod
    def default_severity():
        pass

    @staticmethod
    @abstractmethod
    def applies_to():
        pass

    def __init__(self, severity: Severity):
        self.severity = severity

    @abstractmethod
    def run(self, lookml):
        pass
