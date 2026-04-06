import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ArtifactCard import ArtifactCard


class Deck:
    cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card == card_name:
                self.cards.remove(card_name)
                return True
        return False

    def shuffle(self) -> None:
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Deck is empty")

        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        creature = 0
        spell = 0
        artifact = 0
        for card in self.cards:
            if isinstance(card, CreatureCard):
                creature += 1
            elif isinstance(card, SpellCard):
                spell += 1
            elif isinstance(card, ArtifactCard):
                artifact += 1

        soma = creature + spell + artifact
        avg = soma / 3

        return {
            "total_cards": len(self.cards),
            "creatures": creature,
            "spells": spell,
            "artifacts": artifact,
            "avg_cost": avg}
