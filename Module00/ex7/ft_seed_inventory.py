def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    to_up = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{to_up} seeds: {quantity} packets available")
    elif (unit == "grams"):
        print(f"{to_up} seeds: {quantity} grams total")
    elif (unit == "area"):
        print(f"{to_up} seeds: covers {quantity} square meters")
    else:
        print("Unknown unity type")


def main():
    ft_seed_inventory("tomato", 15, "packets")
    ft_seed_inventory("carrot", 8, "grams")
    ft_seed_inventory("lettuce", 12, "area")
    ft_seed_inventory("Mandioca", 7, "caixas")


if __name__ == "__main__":
    main()
