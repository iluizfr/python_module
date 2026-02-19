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


class SecurePlant:
    def __init__(self):
        pass

    def set_height(self, cm: float):
        if (cm < 0):
            print(f"invalid operation attempted: {cm}cm [REJECTED]")
