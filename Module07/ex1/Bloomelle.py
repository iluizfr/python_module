from ex0.Creature import Creature
from ex1.HealCapability import HealCapability
from typing import Optional


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack_target(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target:  Optional[str] = None) -> str:
        if target is not None:
            return f"Bloomelle heals itself and {target} for a large amount"
        return "Bloomelle heals itself for a large amount"
