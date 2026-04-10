from abc import ABC, abstractmethod
from ex0.Creature import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature) -> list[str]:
        if not self.is_valid(creature):
            message = "for this normal strategy"
            raise Exception(f"Invalid Creature {message}")
        return [creature.attack_target()]

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "attack_target")


class AggressiveStrategy(BattleStrategy):
    def act(self, creature) -> list[str]:
        if not self.is_valid(creature):
            message = "for this aggressive strategy"
            raise Exception(f"Invalid Creature '{creature.name}' {message}")
        return [creature.transform(),
                creature.attack_target(),
                creature.revert()]

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "transform") and hasattr(creature, "revert")


class DefensiveStrategy(BattleStrategy):
    def act(self, creature) -> list[str]:
        if not self.is_valid(creature):
            message = "for this defensive strategy"
            raise Exception(f"Invalid Creature '{creature.name}' {message}")
        return [creature.attack_target(),
                creature.heal()]

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "heal")
