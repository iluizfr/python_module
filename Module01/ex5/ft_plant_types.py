class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        if (self.age >= 30):
            print(f"{self.name} is blooming beautifully!\n")
        else:
            print(f"{self.name} need more time to bloom..\n")

    def display_info(self):
        print(f"{self.name} (Flower): {self.get_info()}, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trnk = trunk_diameter

    def produce_shade(self) -> None:
        a = int(1.56*self.trnk)
        print(f"{self.name} provides {a} square meters of shade\n")

    def display_info(self):
        print(f"{self.name} (Tree): {self.get_info()}, {self.trnk}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: str, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest = harvest_season
        self.nutritional_val = nutritional_value

    def nutri(self) -> None:
        print(f"{self.name} is rich in vitamin {self.nutritional_val}\n")

    def display_info(self):
        print(f"{self.name} (Vegetable): {self.get_info()}, {self.harvest}")


if __name__ == "__main__":
    print("=== Garden Plant Type ===\n")

    rose = Flower("Rose", 25, 30, "red")
    rose.display_info()
    rose.bloom()

    SunFlower = Flower("SunFlower", 75, 44, "yellow")
    SunFlower.display_info()
    SunFlower.bloom()

    Oak = Tree("Oak", 500, 1825, 50)
    Oak.display_info()
    Oak.produce_shade()

    Pine = Tree("Pine", 700, 1234, 30)
    Pine.display_info()
    Pine.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    tomato.display_info()
    tomato.nutri()

    lettuce = Vegetable("Lettuce", 40, 30, "Autunm", "B2")
    lettuce.display_info()
    lettuce.nutri()
