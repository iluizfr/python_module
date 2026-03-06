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
    print(f"Distance between {p0} and {p1}: {calc_distance(p1, p0):.2f}\n")

    p2 = "3,4,0"
    print(f"Parsing coordinates: \"{p2}\"")
    tmp = p2.split(",")
    p3 = (int(tmp[0]), int(tmp[1]), int(tmp[2]))
    print(f"Parsed position: {p3}")
    print(f"Distance between {p0} and {p3}: {calc_distance(p3, p0)}\n")

    if (len(sys.argv) > 1):
        arg = sys.argv[1]
        lista = arg.split(",")
        try:
            p4 = (int(lista[0]), int(lista[1]), int(lista[2]))
        except ValueError:
            print("Only numbers")

    p5 = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{p5}\"")
    tmp2 = p5.split(",")
    try:
        p6 = (int(tmp2[0]), int(tmp2[1]), int(tmp2[2]))
    except ValueError as e:
        print("Error parsing coordinate:", e)
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    print("Unpacking demonstration:")
    x, y, z = (3, 4, 0)
    player = (x, y, z)
    print(f"Player at x={player[0]}, y={player[1]}, z={player[2]}")
    print(f"Cordinates: X={player[0]}, Y={player[1]}, Z={player[2]}")
