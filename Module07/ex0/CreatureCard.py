from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, type: str) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = type

    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {**super().get_card_info(),
                "type": self.type,
                "attack": self.attack,
                "health": self.health}

    def attack_target(target: str) -> str:
        pass
