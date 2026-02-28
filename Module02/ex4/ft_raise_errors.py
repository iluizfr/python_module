class ValueError(Exception):
    pass


class EmptyName(ValueError):
    pass


class WaterError(ValueError):
    pass


class SunError(ValueError):
    pass


def raise_errors(plant_name: str, water_level: int, sun_hours: int) -> None:
    if (not plant_name):
        raise EmptyName("Plant name cannot be empty!")

    if (water_level < 1 or water_level > 10):
        if (water_level > 10):
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        else:
            raise WaterError(f"Water level {water_level} is too low (min 1)")

    if (sun_hours < 2 or sun_hours > 12):
        if (sun_hours < 2):
            raise SunError(f"Sunlight hours {sun_hours} is too low (min 2)")
        else:
            raise SunError(f"sunlight hours {sun_hours} is too high (max 12)")


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    try:
        raise_errors(plant_name, water_level, sunlight_hours)
        print(f"Plant {plant_name} is healthy!\n")
    except EmptyName as e:
        print(f"Error: {e}\n")
    except WaterError as e:
        print(f"Error: {e}\n")
    except SunError as e:
        print(f"Error: {e}\n")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    check_plant_health("Tomato", 6, 4)

    print("Testing empty plant name...")
    check_plant_health(None, 6, 6)

    print("testing bad water level...")
    check_plant_health("Tomato", 15, 4)

    print("Testing bad sunlight hours...")
    check_plant_health("Tomato", 6, 0)

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
