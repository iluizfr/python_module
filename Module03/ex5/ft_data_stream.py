import time
from typing import Generator


def generate_events(n_events: int) -> Generator[str, int, str]:

    players = ["alice", "bob", "charlie", "diana", "luis", "ze", "michal j."]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range(n_events):
        player = players[i % len(players)]
        level = (i % 30) + 1
        event_type = events[i % len(events)]

        yield (player, level, event_type)


def process_stream(n: int) -> None:
    i = 1
    level_up = 0
    high_level = 0
    total_events = 0
    treasure_events = 0
    inicio = time.time()
    stream = generate_events(n)

    print(f"Processing {n} game events...")

    for event in stream:
        total_events += 1
        player, level, event_type = event

        print(f"Event {i}: Player {player} (level {level}) {event_type}")

        if level >= 10:
            high_level += 1
        if event_type == "found treasure":
            treasure_events += 1
        if event_type == "leveled up":
            level_up += 1
        i += 1

    fim = time.time()
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Tresure events: {treasure_events}")
    print(f"Level-up events: {level_up}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {(fim - inicio):.3f} seconds\n")


def fibonacci() -> Generator[int, None, None]:
    a = 0
    b = 1
    while (True):
        yield a
        next_value = a + b
        a = b
        b = next_value


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def generete_prime() -> Generator[int, None, None]:
    i = 2
    while (True):
        if is_prime(i):
            yield i
        i += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    process_stream(1000)

    print("=== Generator Demonstrations ===")
    print("Fibonacci sequence (first 10):", end="")
    fibo = fibonacci()
    for i in range(0, 10):
        print(f" {next(fibo)}", end="")
        if i < 9:
            print(",", end="")
    print("\nPrime numbers (first 5):", end="")
    prime = generete_prime()
    for i in range(0, 10):
        print(f" {next(prime)}", end="")
        if i < 9:
            print(",", end="")
    print()
