from ex0.CreatureFactory import CreatureFactory
from ex1.Sproutling import Sproutling
from ex1.Bloomelle import Bloomelle


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
