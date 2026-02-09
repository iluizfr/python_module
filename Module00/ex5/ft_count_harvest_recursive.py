def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def recursive(c):
        if days == 0:
            return (print("Harvest time!"))
        elif days < 0:
            return
        elif days == c:
            print("Day ", c)
            print("Harvest time!")
            return
        else:
            print("Day ", c)
            recursive(c + 1)
    recursive(1)


def main():
    ft_count_harvest_recursive()


if __name__ == "__main__":
    main()
