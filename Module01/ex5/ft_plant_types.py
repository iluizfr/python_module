class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        if (self.age >= 30):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} need more time to bloom..")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk_diameter

    def produce_shade(self):
        a = int(1.56*self.trunk)
        print(f"{self.name} provides {a} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: str, harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, height, age)
        self.har = harvest_season
        self.nutritional_val = nutritional_value

    def nutri(self):
        print(f"{self.name} is rich in vitamin {self.nutritional_val}")


if __name__ == "__main__":
    print("=== Garden Plant Type ===\n")
    f = Flower("Rose", 25, 30, "red")
    print(f"{f.name} (Flower): {f.height}cm, {f.age} days, {f.color} color")
    f.bloom()
    s = Flower("SunFlower", 75, 44, "yeallow")
    print()
    print(f"{s.name} (Flower): {s.height}cm, {s.age} days, {s.color} color")
    s.bloom()
    print()
    o = Tree("Oak", 500, 1825, 50)
    print(f"{o.name} (Tree): {o.height}cm, {o.age} days, {o.trunk}cm diameter")
    o.produce_shade()
    print()
    p = Tree("Pine", 700, 1234, 30)
    print(f"{p.name} (Tree): {p.height}cm, {p.age} days, {p.trunk}cm diameter")
    p.produce_shade()
    print()
    t = Vegetable("Tomato", 80, 90, "summer", "C")
    print(f"{t.name} (Vegetable): {t.height}cm, {t.age} days, {t.har} harvest")
    t.nutri()
    print()
    v = Vegetable("Lettuce", 40, 30, "Autunm", "B2")
    print(f"{v.name} (Vegetable): {v.height}cm, {v.age} days, {v.har} harvest")
    v.nutri()
