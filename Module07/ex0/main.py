from .CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:\n")
    creature_01 = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(creature_01.get_card_info())

    print("Playing Fire Dragon with 6 mana available:")
    game_state = creature_01.get_card_info()
    creature_01.play(game_state)


if __name__ == "__main__":
    main()
