from ex0.Creature import Creature


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack_target(self) -> str:
        return f"{self.name} uses Hydro Pump!"
