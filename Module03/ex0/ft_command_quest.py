import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    if (len(sys.argv) < 2):
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
    elif (len(sys.argv) >= 2):
        i = 1
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {(len(sys.argv) - 1)}")
        for arg in sys.argv:
            if (i < (len(sys.argv))):
                print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {len(sys.argv)}\n")
