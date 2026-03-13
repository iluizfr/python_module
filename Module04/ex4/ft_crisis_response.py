def read_file(name: str, flag: int) -> None:
    try:
        match flag:
            case 1 | 2:
                print(f"CRISIS ALERT: Attempting access to '{name}'...")
            case 0:
                print(f"\nROUTINE ACCESS: Attempting access to '{name}'...")
        with open(name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        match flag:
            case 0:
                print("STATUS: Normal operations resumed\n")
            case 1:
                print("STATUS: Crisis handled, system stable\n")
            case 2:
                print("STATUS: Crisis handled, security maintained\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        read_file("lost_archive.txt", 1)
        read_file("classified_data.txt", 2)
        read_file("standard_archive.txt", 0)
    finally:
        print("All crisis scenarios handled successfully. Archives secure.")
