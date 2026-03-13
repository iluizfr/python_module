if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    archieve = "new_discovery.txt"
    data_01 = "New quantum algorithm discovered"
    data_02 = "Efficiency increased by 347%"
    data_03 = "Archived by Data Archivist trainee"
    list_data = [data_01, data_02, data_03]
    i = 1

    try:
        print(f"Initializing new storage unit: {archieve}")
        with open(archieve, "w") as file:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            for data in list_data:
                file.write(f"[Entry 00{i}] {data}\n")
                print(f"[Entry 00{i}] {data}")
                i += 1
    except Exception("Something went wrong!") as erro:
        print(f"Error: {erro}")
    finally:
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{archieve}' ready for long-term preservation.")
