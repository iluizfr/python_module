from ex0.Creature import Creature


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack_target(self) -> str:
        return f"{self.name} uses Water Gun!"
