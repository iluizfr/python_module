from abc import ABC, abstractmethod
from typing import Optional


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target:  Optional[str] = None) -> str:
        pass
