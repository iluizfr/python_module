if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    vault = "ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {vault}")
        with open("ancient_fragment.txt", "r") as file:
            content = file.read()
            print("Connection established...\n")
            print(f"RECOVERED DATA:\n{content}")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
    finally:
        print("\nData recovery complete. Storage unit disconnected.")
