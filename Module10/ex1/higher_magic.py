from typing import Callable


Spell = Callable[[str,  int], str]


def spell_combiner(spell1: Spell,
                   spell2: Spell) -> Callable[[str, int], tuple[str, str]]:
    def new_func(target:  str, power: int):
        return (spell1(target, power), spell2(target, power))
    return new_func


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    def new_func(target: str, power):
        return base_spell(target, power * multiplier)
    return new_func


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Spell) -> Spell:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def enough_power(target: str, power: int) -> bool:
    return power > 10


def main() -> None:
    print("Testing spell combiner..")
    combined = spell_combiner(heal, fireball)
    act = combined("dragon", 10)
    for a in act:
        print(a)

    print("\nTesting power amplifier..")
    print(f"Original: {fireball("dragon", 10)}", end=", ")
    amplified = power_amplifier(fireball, 2)
    print("Amplified:", amplified("dragon", 10))

    print("\nTesting conditional caster..")
    print("Dragon have enough power:", end="")
    test = conditional_caster(enough_power, fireball)
    print(test("dragon", 10))

    print("\nTesting spell sequence..")
    sequence = spell_sequence([heal, fireball])
    result = sequence("dragon", 10)
    for i in result:
        print(i)


if __name__ == "__main__":
    main()
