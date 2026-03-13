# Set is a collection which is unordered, unchangeable*
# "can add or remove", and unindexed. No duplicate members.
class Player:
    def __init__(self, name: str, achievements: set) -> None:
        self.name = name
        self.achievements = achievements

    def get_info(self) -> None:
        print(f"Player {self.name} achievements: {self.achievements}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = Player("alice", {"first_kill", "level_10", "treasure_hunter",
                   "speed_demon"})
    bob = Player("bob", {'first_kill', 'level_10', 'boss_slayer', 'collector'})
    charlie = Player("charlie", {'level_10', 'treasure_hunter', 'boss_slayer',
                                 'speed_demon', 'perfectionist'})

    alice.get_info()
    bob.get_info()
    charlie.get_info()

    print("\n=== Achievement Analytics ===")
    uniques = alice.achievements.union(bob.achievements, charlie.achievements)
    print(f"All unique achievemets: {uniques}")
    print(f"Total unique achievements: {len(uniques)}\n")

    inter = alice.achievements.intersection(bob.achievements,
                                            charlie.achievements)
    print(f"Common to all players: {inter}")

    rare_alice = alice.achievements.difference(
        bob.achievements.union(charlie.achievements))

    rare_bob = bob.achievements.difference(
        alice.achievements.union(charlie.achievements))

    rare_charlie = charlie.achievements.difference(
        alice.achievements.union(bob.achievements))

    rare = rare_alice | rare_bob | rare_charlie  # | == union

    print(f"Rare achievements (1 player): {rare}")

    common_alice_bob = alice.achievements.intersection(bob.achievements)
    print(f"\nAlice vc Bob common: {common_alice_bob}")

    alice_unique = alice.achievements - bob.achievements  # - == difference
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob.achievements - alice.achievements
    print(f"Bob unique: {bob_unique}")
