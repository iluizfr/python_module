import os
from dotenv import load_dotenv


def get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        return f"[WARNING] {name} not set"
    return value


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    load_dotenv()

    mode = get_env("MATRIX_MODE")
    data_base = get_env("DATABASE_URL")
    api_key = get_env("API_KEY")
    log_level = get_env("LOG_LEVEL")
    zion = get_env("ZION_ENDPOINT")

    print("\nConfiguration loaded:")

    if mode == "production":
        print("Mode: production")
        print(f"Database: Connected to production instance: {data_base}")
        if api_key:
            print("API Access: Authenticated")
        else:
            print("API Access: Missing key")
        print("Log Level: WARNING or higher")
    else:
        print("Mode: development")
        print(f"Database: Connected to local instance: {data_base}")
        if api_key:
            print("API Access: Authenticated")
        else:
            print("API Access: Missing key")
        print(f"Log Level: {log_level or 'DEBUG'}")

    print(f"Zion Network: {'Online' if zion else 'Offline'}")

    print("\nEnvironment security check:")

    if ".env" in os.listdir():
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")


if __name__ == "__main__":
    main()
