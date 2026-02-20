class SecurePlant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name = name
        print(f"Plant created: {name}")
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, cm: float):
        if (cm < 0):
            print(f"\ninvalid operation attempted: height {cm}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height += cm
            print(f"Height update: {self.__height}cm [OK]")

    def set_age(self, age: int):
        if (age < 0):
            print(f"\ninvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age += age
            print(f"Age update: {self.__age} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_info(self):
        return f"{self.__name} ({self.get_height()}cm, {self.get_age()} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant.get_info()}")
