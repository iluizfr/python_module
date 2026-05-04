from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not len(spells):
        return 0

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in operations:
        raise ValueError("Unknow operation")

    return reduce(operations[operation], spells)  # type: ignore


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    aqua = partial(base_enchantment, 50, "Aqua")
    fire = partial(base_enchantment, 50, "Fire")
    rock = partial(base_enchantment, 50, "Rock")
    return {
        "Aqua": aqua,
        "Fire": fire,
        "Rock": rock
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknow spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantme: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multicast: {len(spell)} spells"

    return dispatch


def enchantmet(power: int, element: str, target: str) -> str:
    return f"Echants {power} of element {element} in {target}"


def main() -> None:
    print("Testing spell reducer...")
    try:
        spells = [10, 20, 30, 40]
        print("Sum:", spell_reducer(spells, "add"))
        print("Product:", spell_reducer(spells, "multiply"))
        print("Max:", spell_reducer(spells, "max"))
    except ValueError as err:
        print(err)

    print("\nTesting partial enchanter...")
    encantamentos = partial_enchanter(enchantmet)
    agua = encantamentos["Aqua"]
    print(agua("Sword"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    caster = spell_dispatcher()
    print(caster(42))
    print(caster("fireball"))
    print(caster([10, "fire-water", 2]))
    print(caster(3.14))


if __name__ == "__main__":
    main()
