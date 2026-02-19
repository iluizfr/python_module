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


if __name__ == "__main__":
    cm: int = 6
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant.get_info()
    plant.grow(cm)
    plant.aged(6)
    print("=== Day 7 ===")
    plant.get_info()
    print(f"Growth this week: +{cm}cm")
