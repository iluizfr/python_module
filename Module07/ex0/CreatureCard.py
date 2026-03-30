from ex0.Card import Card


class CreatureCard(Card):
	def __init__(self, name: str, cost: int, rarity: str,
			  attack: int, health: int) -> None:
              super().__init__(name: str, cost: int, rarity: str)
