from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")

    print("Building deck with different card types...")

    spell = SpellCard("Lightning Bolt", 3, "Common", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "Rare", 1, "+1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, "Rare", 6, 7)
    deck = Deck()

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    print(deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")
    card_01 = deck.draw_card()
    print(f"Drew: {card_01}, ({card_01.kind})")
    