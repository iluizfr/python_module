# Dictionary is a collection which is ordered** and
# changeable. No duplicate members.
import sys


class NegativeError(Exception):
    pass


def parser(args: list) -> dict:
    inventory = {}

    for arg in args:
        if ':' in arg:
            key, value = arg.split(':', 1)
            try:
                tmp = int(value)
                if tmp < 0:
                    raise NegativeError("Cannot acept negative integers..")
                inventory[key] = int(value)
            except ValueError as erro_1:
                print(f"Error: Only numbers for quantities: {erro_1}")
            except NegativeError as erro_2:
                print(f"Error: Only positive numbers: {erro_2}")
    return inventory


def calc_info(invetory: dict) -> None:
    print("=== Inventory System Analysis ===")
    list_values = inventory.values()
    units = 0
    for value in list_values:
        units += value

    print(f"Total items in inventory: {units}")
    print("Unique item types:", len(inventory))

    print("\n=== Current Inventory ===")
    for key, value in inventory.items():
        print(f"{key}: {value} units ({value / units * 100:.2f})")

    print("\n=== Inventory Statistics ===")
    bigger_value = 0
    bigger_key = None
    for key, value in inventory.items():
        if value > bigger_value:
            bigger_value = value
            bigger_key = key
    print(f"Most abundant: {bigger_key} ({bigger_value} units)")

    smaller_value = bigger_value
    smaller_key = None
    for key, value in inventory.items():
        if value < smaller_value:
            smaller_value = value
            smaller_key = key
    print(f"Least abundant: {smaller_key} ({smaller_value} units)")

    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}
    for key, value in inventory.items():
        if value > 3:
            moderate[key] = value
        else:
            scarce[key] = value
    print("Moderate:", moderate)
    print("Scarce:", scarce)

    print("\n=== Management Suggestions ===")
    restock = []
    for key, value in inventory.items():
        if value < 2:
            restock += [key]

    if (len(restock) > 0):
        i = 0
        print("Restock needed:", end=" ")
        for item in restock:
            print(item, end="")
            i += 1
            if i < len(restock):
                print(", ", end="")

    print("\n\n=== Dictionary Properties Demo ===")
    keys = inventory.keys()
    values = inventory.values()
    print("Dictionary keys:", end=" ")
    j = 0
    for key in keys:
        print(key, end="")
        j += 1
        if j < len(keys):
            print(", ", end="")

    print("\nDictionary values:", end=" ")
    j = 0
    for value in values:
        print(value, end="")
        j += 1
        if j < len(values):
            print(", ", end="")

    print(f"\nSample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    args = sys.argv[1:]
    inventory = parser(args)
    calc_info(inventory)
