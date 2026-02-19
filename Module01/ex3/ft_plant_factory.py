class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, cm: int) -> None:
        self.height += cm

    def aged(self, days: int) -> None:
        self.age += days


class Factory():
    def __init__(self):
        self.plants = []

    def add_plant(self, name: str, height: float, age: int):
        new_plant = Plant(name, height, age)
        self.plants += [new_plant]

    def factory_info(self):
        i = 0
        print("=== Plant Factory Output ===")
        for plant in self.plants:
            print(f"Created: {plant.name} ({plant.height}cm {plant.age} days)")
            i += 1
        print(f"\nTotal plants created: {i}")


if __name__ == "__main__":
    factory = Factory()
    factory.add_plant("Rose", 25, 30)
    factory.add_plant("Oak", 200, 365)
    factory.add_plant("Cactus", 5, 90)
    factory.add_plant("Sunflower", 80, 45)
    factory.add_plant("Fern", 15, 120)
    factory.factory_info()
