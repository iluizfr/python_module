from ex0.AquaFactory import AquaFactory
from ex0.CreatureFactory import CreatureFactory
from ex0.FlameFactory import FlameFactory
from ex1.HealingCreatureFactory import HealingCreatureFactory
from ex1.TransformCreatureFactory import TransformCreatureFactory
from ex2.Strategy import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.Strategy import BattleStrategy


def battle(creatures: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(creatures)} opponents involved")

    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            factory01, strategy01 = creatures[i]
            factory02, strategy02 = creatures[j]

            creature01 = factory01.create_base()
            creature02 = factory02.create_base()

            print("\n* Battle *")
            print(f"{creature01.describe()}\n vs.")
            print(f"{creature02.describe()}")
            print(" now fight!")

            try:
                action1 = strategy01.act(creature01)
                action2 = strategy02.act(creature02)

                for action in action1:
                    print(action)
                for action in action2:
                    print(action)

            except Exception as error:
                print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    creatures = [(FlameFactory(), NormalStrategy()),
                 (HealingCreatureFactory(), DefensiveStrategy())]
    battle(creatures)

    print("\nTornament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    cretures2 = [(FlameFactory(), AggressiveStrategy()),
                 (HealingCreatureFactory(), DefensiveStrategy())]
    battle(cretures2)

    print("\nTornament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    creatures3 = [(AquaFactory(), NormalStrategy()),
                  (HealingCreatureFactory(), DefensiveStrategy()),
                  (TransformCreatureFactory(), AggressiveStrategy())]
    battle(creatures3)


if __name__ == "__main__":
    main()
