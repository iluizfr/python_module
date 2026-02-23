class InvalidPlant(Exception):
    pass


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise InvalidPlant("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except InvalidPlant as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system(plants: list) -> None:
    try:
        water_plants(plants)
    except InvalidPlant:
        pass
    finally:
        if None not in plants:
            print("Watering completed successfully")
        else:
            print("\nCleanup aways happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    plants = ["Banana", "Goiaba", "Abacaxi"]
    plants2 = ["Tomato", None]

    print("\nTesting normal watering...")
    test_watering_system(plants)

    print("\nTesting with error...")
    test_watering_system(plants2)
