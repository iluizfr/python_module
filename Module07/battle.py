from ex0.CreatureFactory import CreatureFactory
import ex0


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack_target())

    print(evolved.describe())
    print(evolved.attack_target())


def battle(flame_fac: CreatureFactory, aqua_fac: CreatureFactory) -> None:
    flameling = flame_fac.create_base()
    aquabub = aqua_fac.create_base()

    print(flameling.describe())
    print("vs.")
    print(aquabub.describe())
    print(" fight!")
    print(flameling.attack_target())
    print(aquabub.attack_target())


def main() -> None:
    print("Testing Factory")
    flame_factory = ex0.FlameFactory()
    test_factory(flame_factory)

    print("\nTesting Factory")
    water_factory = ex0.AquaFactory()
    test_factory(water_factory)

    print("\nTesting battle")
    battle(flame_factory, water_factory)


if __name__ == "__main__":
    main()
