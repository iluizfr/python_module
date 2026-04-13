import sys
import os
import site


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:

    if not is_in_venv():
        print("\nMATRIX STATUS: You're still plugged in\n")

        print("Current Python:", sys.base_prefix)
        print("Virtual Environment: None detected")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")

        print("Then run this program again.")

    elif is_in_venv():
        print("\nMATRIX STATUS: Welcome to the construct\n")

        print("Current Python:", sys.base_prefix)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("Environment Pat:", os.environ.get("VIRTUAL_ENV"))

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system\n")

        print("Package installation path:")
        print(site.getsitepackages())


if __name__ == "__main__":
    main()
