from ex0.Creature import Creature
from ex1.TransformCapability import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.is_transformed = False

    def attack_target(self) -> str:
        if not self.is_transformed:
            return "Shiftling attacks normally."
        return "Shiftling performs a boosted strike!"

    def transform(self) -> str:
        if not self.is_transformed:
            self.is_transformed = True
            return "Shiftling shifts into a sharper form!"
        return "Shiftling already trasfored."

    def revert(self) -> str:
        self.is_transformed = False
        return "Shiftling returns to normal."
