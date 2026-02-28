class ErrorName(Exception):
    pass


class InvalidPlant(Exception):
    pass


class EmptyName(Exception):
    pass


class WaterError(Exception):
    pass


class SunError(Exception):
    pass


class GardenError(Exception):
    pass


class Plant:
    def __init__(self, name: str, height: float, age: int,
                 water: int, sun: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.water = water
        self.sun = sun


def validate_name(name: str) -> None:
    if not name:
        raise ErrorName("plant name cannot be empty!")


def check_tank(tank: int):
    if tank < 30:
        raise GardenError("Not enugh water in tank")


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


class GardenManager:
    def __init__(self) -> None:
        self.plants = []
        self.water_tank = 30

    def add_plant(self, plant: Plant) -> None:
        try:
            validate_name(plant.name)
            self.plants += [plant]
            print(f"Added {plant.name} successfully")
        except ErrorName as e:
            print(f"Error adding plant: {e}", end="\n\n")

    def water_plants(self, plants: list) -> None:
        print("Opening watering system")
        try:
            for plant in plants:
                if plant is None:
                    raise InvalidPlant("Cannot water None - invalid plant!")
                print(f"Watering {plant.name} - sucess")
                self.water_tank -= 1
        except InvalidPlant as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self) -> None:
        try:
            for plant in self.plants:
                raise_errors(plant.name, plant.water, plant.sun)
                print(f"{plant.name}: healthy (water: {plant.water}", end="")
                print(f", sun: {plant.sun})")
        except EmptyName as e:
            print(f"Error checking {plant.name}: {e}\n")
        except WaterError as e:
            print(f"Error checking {plant.name}: {e}\n")
        except SunError as e:
            print(f"Error checking {plant.name}: {e}\n")

    def error_recovery(self) -> None:
        try:
            check_tank(self.water_tank)
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...\n")


def test_garden_management():
    print("=== garden management System ===\n")

    garden = GardenManager()
    tomato = Plant("tomato", 30, 30, 5, 8)
    lettuce = Plant("lettuce", 30, 30, 15, 10)
    erro_plant = Plant(None, 30, 30, 0, 0)

    print("Adding plants to garden...")
    garden.add_plant(tomato)
    garden.add_plant(lettuce)
    garden.add_plant(erro_plant)

    print("Watering plants...")
    garden.water_plants(garden.plants)

    print("Checking plant health...")
    garden.check_plant_health()

    print("Testing error recovery...")
    garden.error_recovery()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
