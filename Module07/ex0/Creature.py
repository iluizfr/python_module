from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.creature_type = creature_type
        self.name = name

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"

    def _validate_str(str_input: str) -> str:
        if type(str_input) is not str or str_input.strip():
            raise ValueError("Error")
        return str_input

    @abstractmethod
    def attack_target(self) -> str:
        pass
