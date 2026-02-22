def check_temperature(temp_str: str):
    try:
        print(f"Testing temperature: {temp_str}")
        n = int(temp_str)
        if (n > 0 and n < 40):
            return print(f"Temperature {n}°C is perfect for plants!\n")
        else:
            if (n < 0):
                print(f"Error: {n}°C is too cold for plants (min 0°C)\n")
            elif (n > 40):
                print(f"Error: {n}°C is too hot for plants (max 40°C)\n")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input(tests: list) -> None:
    print("=== Garden Temperature Checker ===\n")
    for test in testes:
        if (check_temperature(test)):
            print(f"{check_temperature(test)}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    testes = ["25", "abc", "100", "50"]
    test_temperature_input(testes)
