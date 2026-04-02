from .CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    creature_01 = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(creature_01.get_card_info())

    game_state = creature_01.get_card_info()
    creature_01.play(game_state, 6)

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack Result: {creature_01.attack_target("Goblin Warrior")}")

    print("\nTesting insufficient mana (3 available):")
    creature_01.play(game_state, 3)

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
