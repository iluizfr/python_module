# Tuple is a collection which is ordered
# and unchangeable. Allows duplicate members.
import sys
import math


def calc_dist(pos1: tuple, pos2: tuple) -> float:
    return math.sqrt(
                    (pos2[0] - pos1[0]) ** 2 +
                    (pos2[1] - pos1[1]) ** 2 +
                    (pos2[2] - pos1[2]) ** 2)


def parser(argv: str) -> None:
    p0 = (0, 0, 0)

    if (len(sys.argv) > 1):
        try:
            arg = sys.argv[1].split(",")
            arg = (int(arg[0]), int(arg[1]), int(arg[2]))
            print(f"Parsing coordinates: \"{arg}\"")
            print(f"Parsed position: {p3}")
            print(f"Distance between {p0} and {arg}: {calc_dist(arg, p0)}\n")
        except ValueError as e:
            print(f"Parsing invalid coordinates: \"{arg}\"")
            print("Error parsing coordinate:", e)
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    p0 = (0, 0, 0)
    p1 = (10, 20, 5)
    print(f"Position created: {p1}")
    print(f"Distance between {p0} and {p1}: {calc_dist(p1, p0):.2f}\n")

    p2 = "3,4,0"
    print(f"Parsing coordinates: \"{p2}\"")
    tmp = p2.split(",")
    p3 = (int(tmp[0]), int(tmp[1]), int(tmp[2]))
    print(f"Parsed position: {p3}")
    print(f"Distance between {p0} and {p3}: {calc_dist(p3, p0)}\n")

    parser(sys.argv[1])

    print("\nUnpacking demonstration:")
    x, y, z = (3, 4, 0)
    player = (x, y, z)
    print(f"Player at x={player[0]}, y={player[1]}, z={player[2]}")
    print(f"Cordinates: X={player[0]}, Y={player[1]}, Z={player[2]}")
