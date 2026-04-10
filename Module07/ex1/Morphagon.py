from ex0.Creature import Creature
from ex1.TransformCapability import TransformCapability


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_transformed = False

    def attack_target(self) -> str:
        if not self.is_transformed:
            return "Morphagon attacks normally."
        return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        if not self.is_transformed:
            self.is_transformed = True
            return "Morphagon morphs into a dragonic battle form!"
        return "Morphagon already trasfored."

    def revert(self) -> str:
        self.is_transformed = False
        return "Morphagon stabilizes its form."
