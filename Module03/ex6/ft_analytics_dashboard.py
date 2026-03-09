class Player:
    def __init__(self, name: str, score: int, is_active: bool):
        self.name = name
        self.score = score
        self.is_active = is_active


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")

    list_player = [Player('alice', 2300, True),
                   Player('charlie', 2150, True),
                   Player('diana', 2050, False),
                   Player('bob', 1800, True)]
    scores = [p.score for p in list_player]
    high_scores = []
    doubles = []
    actives = []

    for player in list_player:
        if player.score > 2000:
            high_scores += [player.name]

    for score in scores:
        doubles += [score * 2]

    for player in list_player:
        if player.is_active is True:
            actives += [player.name]

    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {doubles}")
    print(f"Active players: {actives}")

    print("\n=== Dict Comprehension Examples ===")

    players_dict = {
        'alice': 2300,
        'bob': 1800,
        'charlie': 2150
        }
    print(f"Players and scores: {players_dict}")

    bigger = max(players_dict.values())
    best_player: str = None
    for key, value in players_dict.items():
        if value == bigger:
            best_player = key
    print(f"Best player: {key}")

    values = players_dict.values()
    total_score = 0
    for score in values:
        total_score += score

    n_players = len(players_dict)
    avarege = total_score / n_players
    print(f"Avarege players score: {avarege:.0f}")
    print(f"Total score: {total_score}")

    print("\n=== Set Comprehension Examples ===")

    players_set = {'alice', 'bob', 'charlie', 'diana', 'diana'}
    print(f"Unique players: {players_set}")
    print(f"Testing if player 'michel' is in set: {'michel' in players_set}")
    