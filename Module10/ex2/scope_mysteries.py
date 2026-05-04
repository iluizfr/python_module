from typing import Callable


def mage_counter() -> Callable[[], int]:
    i = 0

    def counter() -> int:
        nonlocal i
        i += 1
        return i
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    x = initial_power

    def accumulator(add_power: int) -> int:
        nonlocal x
        x += add_power
        return x
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    enchan = enchantment_type

    def factory(item_name: str) -> str:
        nonlocal enchan
        return f"{enchan} {item_name}"
    return factory


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        vault[key] = value

    def recall(key: str) -> int | None | str:
        if key in vault.keys():
            return vault.get(key)
        else:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("Testing mage counter...")
    a = mage_counter()
    b = mage_counter()
    print("counter_a call 1:", a())
    print("counter_a call 2:", a())
    print("counter_b call 1:", b())

    print("\nTesting spell accumulator...")
    y = spell_accumulator(100)
    i = y(20)
    print(f"Base 100, add 20: {i}")
    i = y(30)
    print(f"Base 100, add 30: {i}")

    print("\nTesting enchantment factory...")
    flame = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flame("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    mv = memory_vault()
    print("store 'secret' = 42")
    mv["store"]("secret", 42)
    print("Recall 'secret':", mv["recall"]("secret"))
    print("Recall 'Unknow':", mv["recall"]("Unknow"))


if __name__ == "__main__":
    main()
