class GardenError(Exception):
	pass


class PlantError(GardenError):
	pass


class WaterError(GardenError):
	pass


def garden_problem(flag: int) -> None:
	if (flag == 1):
		raise GardenError("Something wrong in the garden!\n")


def plant_problem(flag: int) ->None:
	if (flag == 1):
		raise PlantError("The tomato plant is wilting!\n")


def water_problem(flag: int):
	if (flag == 1):
		raise WaterError("Not enough water in the tank!\n")


def test_errors(problens: list):
	print("=== Custom Garden Errors Demo ===\n")
	for problem in problens:
		print(f"Testing {problem}...")
		



if __name__ == "__main__":
