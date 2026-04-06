from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.kind = "Artifact"

    def play(self, game_state: dict) -> dict:
        self.durability -= 1
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"}

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {
                "status": "destroyed",
                "effect": "none"}
        else:
            return {
                "artifact": f"{self.name}",
                "effect": f"{self.effect}",
                "durability_left": f"{self.durability}"}
