import sys


if __name__ == "__main__":
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n\n")
    alert_01 = "Communication channels verified"

    try:
        id = input("Input Stream active. Enter archivist ID: ")
        report = input("Input Stream active. Enter status: ")
        if (id.strip() == "" or report.strip() == ""):
            raise ValueError("Empty arg are not allowed.")

    except ValueError as err:
        sys.stderr.write(f"[STDERR] {err}")
        sys.exit()
    sys.stdout.write(f"\n[STANDARD] Archive status from {id}: {report}\n")
    sys.stdout.write(f"[ALERT] System diagnostic: {alert_01}\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.\n")
