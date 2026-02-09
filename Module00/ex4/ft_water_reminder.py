def ft_water_reminder():
    day = int(input("Days since last watering: "))
    if (day > 2):
        print("Water the plants!")
    elif (day >= 0):
        print("Plants are fine")


def main():
    ft_water_reminder()


if __name__ == "__main__":
    main()
