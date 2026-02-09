def harvest_total():
    sum = 0
    day = 1
    for i in range(3):
        sum += int(input(f"Day {day} havest: "))
        day += 1

    print("Total harvest: ", sum)


def main():
    harvest_total()


if __name__ == "__main__":
    main()
