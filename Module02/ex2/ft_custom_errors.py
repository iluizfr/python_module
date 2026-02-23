class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant_problem(flag: int) -> None:
    if (flag == 1):
        try:
            raise PlantError("The tomato plant is wilting!")
        except PlantError as e:
            print(f"Caught PlantError: {e}")


def water_problem(flag: int) -> None:
    if (flag == 1):
        try:
            raise WaterError("Not enough water in the tank!")
        except WaterError as e:
            print(f"Caught WaterError: {e}")


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlanError...")
    try:
        plant_problem(1)
    except PlantError as e:
        print(f"Caught a PlantError: {e}")
    print("\nTesting WaterProblem...")
    try:
        water_problem(1)
    except WaterError as e:
        print(f"Caught a WaterError: {e}\n")
    print("\nTesting catching all garden errors...")
    for func in (plant_problem, water_problem):
        try:
            func(1)
        except GardenError as e:
            print(f"Caught a GardenError: {e}")
    print("\nAll custum error types work correctly!")


if __name__ == "__main__":
    test_errors()
