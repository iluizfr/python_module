def ft_plant_age() -> None:
    age = int(input("Enter plant age in days: "))
    if (age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")


def main():
    ft_plant_age()


if __name__ == "__main__":
    main()
