def garden_summary() -> None:
    garden_name = input("Enter garden name: ")
    n = int(input("Enter number of plants: "))
    print("Garden:", garden_name)
    print("Plants:", n)
    print("Status: Growing well!")


def main():
    garden_summary()


if __name__ == "__main__":
    main()
