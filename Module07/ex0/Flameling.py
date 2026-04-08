from ex0.Creature import Creature


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack_target(self) -> str:
        return f"{self.name} uses Ember!"
