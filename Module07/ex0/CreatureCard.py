from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = self.validate_value(attack)
        self.health = self.validate_value(health)
        self.type = "Creature"

    def play(self, game_state: dict, mana: int = 0) -> dict:
        if mana < self.cost:
            print(f"Playable: {self.is_playable(mana)}")
            return game_state
        else:
            print(f"Playable: {self.is_playable(mana)}")
            result = {"card_played": self.name, "mana_used": mana,
                      "effect": "Creature summoned to battlefield"}
            print(f"Play result: {result}")
            return result

    def get_card_info(self) -> dict:
        return {**super().get_card_info(),
                "type": self.type,
                "attack": self.attack,
                "health": self.health}

    def attack_target(self, target: str) -> dict:
        return {"attacker": self.name, "target": target,
                "damage_dealt": self.attack, "combat_resolved": True}
