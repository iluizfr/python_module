from ex0.Creature import Creature


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack_target(self) -> str:
        return f"{self.name} uses Flamethrower!"
