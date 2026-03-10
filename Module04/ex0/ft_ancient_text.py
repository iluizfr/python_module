if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    vault = "ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {vault}")
        with open("ancient_fragment.txt", "r") as f:
            content = f.read()
            print("Connection established...\n")
            print(f"RECOVERED DATA:\n{content}")
    except FileNotFoundError as error:
        print(error)
    finally:
        print("\nData recovery complete. Storage unit disconnected.")
