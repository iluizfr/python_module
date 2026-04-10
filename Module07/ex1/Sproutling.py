from ex0.Creature import Creature
from ex1.HealCapability import HealCapability
from typing import Optional


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack_target(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target:  Optional[str] = None) -> str:
        if target is not None:
            return f"Sproutling heals itself and {target} for a small amount"
        return "Sproutling heals itself for a small amount"
