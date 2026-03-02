import sys
import math


def calc_distance(pos1: tuple, pos2: tuple) -> float:
    return math.sqrt(
                    (pos2[0] - pos1[0]) ** 2 +
                    (pos2[1] - pos1[1]) ** 2 +
                    (pos2[2] - pos1[2]) ** 2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    p0 = (0, 0, 0)
    p1 = (10, 20, 5)
    print(f"Position created: {p1}")
    print(f"Distance between {p0} and {p1}: {calc_distance(p1, p0)}\n")

    arg = sys.argv[1]
    lista = arg.split(",")
    try:
        p2 = (int(lista[0]), int(lista[1]), int(lista[2]))
    except ValueError:
        print