class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        self.height += cm

    def get_info(self):
        return f"{self.name} | Height: {self.height}cm | Age: {self.age}"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        return f"{super().get_info()} | Color: {self.color}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: float, age: int, color: str,
                 prize) -> None:
        super().__init__(name, height, age, color)
        self.prize_level = prize


class GardenManager:
    class GardenStats:
        def __init__(self, plants: list) -> None:
            self.plants = plants

        def garden_len(self):
            plant: int = 0
            for plant in self.plants:
                plant += 1
                return plant

    def __init__(self, name: str):
        self.name = name
        self.plants = []

    def add_plant(self, plant: Plant)
        self.plants += [plant]


if __name__ == "__main__":
    pass