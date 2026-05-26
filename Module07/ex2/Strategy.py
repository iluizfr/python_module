from abc import ABC, abstractmethod
from ex0.Creature import Creature
from ex1.TransformCapability import TransformCapability
from ex1. HealCapability import HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            message = "for this normal strategy"
            raise Exception(f"Invalid Creature {message}")
        return [creature.attack_target()]

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "attack_target")


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            message = "for this aggressive strategy"
            raise Exception(f"Invalid Creature '{creature.name}' {message}")
        if isinstance(creature, TransformCapability):
            return [creature.transform(),
                    creature.attack_target(),
                    creature.revert()]
        raise ValueError(f"Invalid Creature '{creature.name}' {message}")

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "transform") and hasattr(creature, "revert")


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            message = "for this defensive strategy"
            raise Exception(f"Invalid Creature '{creature.name}' {message}")
        if isinstance(creature, HealCapability):
            return [creature.attack_target(),
                    creature.heal()]
        raise ValueError(f"Invalid Creature '{creature.name}' {message}")

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "heal")
