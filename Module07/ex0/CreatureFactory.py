from abc import ABC, abstractmethod
from ex0.Creature import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base() -> Creature:
        pass

    @abstractmethod
    def create_evolved() -> Creature:
        pass
