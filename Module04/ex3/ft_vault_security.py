if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    vault_01 = "ft_vault_security.py"
    vault_02 = "preservation.txt"

    try:
        print("Initiating secure vault access...")
        with open(vault_01, "r") as file:
            print("Vault connection established with failsafe protocols\n")

            print("SECURE EXTRACTION:")
            print(file.read())
            print("[CLASSIFIED] Quantum encryption keys recovered")
            print("[CLASSIFIED] Archive integrity: 100%")

        print("\nSECURE PRESERVATION:")
        with open(vault_02, "w") as file_02:
            file_02.write("New data preserved.")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")
    except FileNotFoundError as err:
        print(err)
    finally:
        print("\nAll vault operations completed with maximum security.")
