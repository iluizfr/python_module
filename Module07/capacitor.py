from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")
    print(" base:")

    heal_factory = HealingCreatureFactory()
    base = heal_factory.create_base()
    evolved = heal_factory.create_evolved()

    print(base.describe())
    print(base.attack_target())
    print(base.heal())

    print(" evolved:")

    print(evolved.describe())
    print(evolved.attack_target())
    print(evolved.heal("others"))

    print("\nTesting Creature with transform capability")
    print(" base:")
    trans_factory = TransformCreatureFactory()
    base_02 = trans_factory.create_base()
    print(base_02.describe())
    print(base_02.attack_target())
    print(base_02.transform())
    print(base_02.attack_target())
    print(base_02.revert())

    print(" evolved:")
    evolved_02 = trans_factory.create_evolved()
    print(evolved_02.describe())
    print(evolved_02.attack_target())
    print(evolved_02.transform())
    print(evolved_02.attack_target())
    print(evolved_02.revert())


if __name__ == "__main__":
    main()
