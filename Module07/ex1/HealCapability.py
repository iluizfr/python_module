from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(target: str):
        pass
