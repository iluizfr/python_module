def ft_count_havesdt_iterative():
    c = 1
    days = int(input("Days until harvest: "))
    for days in range(0, days):
        print("Day ", c)
        c += 1
    print("Harvest time!")


def main():
    ft_count_havesdt_iterative()


if __name__ == "__main__":
    main()
