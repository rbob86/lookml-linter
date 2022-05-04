from abc import ABC, abstractmethod


class Rule(ABC):
    @abstractmethod
    def run(self, lookml):
        pass
