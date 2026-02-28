class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = True

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: float, age: int, color: str,
                 prize_points) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.prize_points}"


class GardenManager:
    total_gardens = 0

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        self.plants_added = 0
        GardenManager.total_gardens += 1

    class GardenStats:
        def __init__(self, plants: list) -> None:
            self.plants = plants

        def count_regular(self) -> int:
            count = 0
            for plant in self.plants:
                if type(plant) is Plant:
                    count += 1
            return count

        def count_flowering(self) -> int:
            count = 0
            for plant in self.plants:
                if (isinstance(plant, FloweringPlant)
                        and not isinstance(plant, PrizeFlower)):
                    count += 1
            return count

        def count_prize(self) -> int:
            count = 0
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    count += 1
            return count

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        self.plants_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_plants_grow(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def show_reports(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")

        print(f"\nPlants added: {self.plants_added},", end="")
        print(f"Total growth {self.total_growth}cm")

        stats = self.GardenStats(self.plants)
        regular = stats.count_regular()
        flowering = stats.count_flowering()
        prize = stats.count_prize()

        print(f"Plants type: {regular} regular,", end="")
        print(f" {flowering} flowering,", end="")
        print(f" {prize} prize flowers")

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(height) -> bool:
        return height >= 0

    def calculate_score(self) -> int:
        score = 0
        for plant in self.plants:
            score += plant.height
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score


if __name__ == "__main__":
    print("=== Garden Manager System Demo ===\n")

    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    oak = Plant("Oak Tree", 100, 5)
    rose = FloweringPlant("Rose", 25, 2, "red")
    sunflower = PrizeFlower("SunFlower", 50, 1, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.help_all_plants_grow()
    alice_garden.show_reports()

    print("\nHeight validation test: ", GardenManager.validate_height(20))
    print(f"Garden scores - Alice: {alice_garden.calculate_score()}, ", end="")
    print(f"Bob: {bob_garden.calculate_score()}")

    GardenManager.create_garden_network()
