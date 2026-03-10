class Player:
    def __init__(self, name: str, score: int, is_active: bool,
                 achieves: set) -> None:
        self.name = name
        self.score = score
        self.is_active = is_active
        self.achieves = achieves


def list_examples() -> None:
    print("=== List Comprehension Examples ===")

    list_player = [Player('alice', 2300, True, None),
                   Player('charlie', 2150, True, None),
                   Player('diana', 2050, False, None),
                   Player('bob', 1800, True, None)]
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


def dict_examples() -> None:
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
    print(f"Best player: {best_player}")

    values = players_dict.values()
    total_score = 0
    for score in values:
        total_score += score

    n_players = len(players_dict)
    avarege = total_score / n_players
    print(f"Avarege players score: {avarege:.0f}")
    print(f"Total score: {total_score}")


def set_examples() -> None:
    print("\n=== Set Comprehension Examples ===")

    achieves_set = {'first_kill', 'level_10', 'level_10', 'treasure_hunter',
                    'speed_demon', 'boss_slayer', 'collector', 'perfectionist'}
    players_set = {Player('alice', 2300, True, achieves_set),
                   Player('charlie', 2150, True, achieves_set),
                   Player('diana', 2050, False, achieves_set),
                   Player('bob', 1800, True, achieves_set)}

    set_of_names = set((player.name for player in players_set))

    print(f"Unique players: {set_of_names}")
    print(f"Testing if player 'michel' is in set: {'michel' in set_of_names}")
    print(f"Unique and shufled achievements {achieves_set}")


def combined_analysis() -> None:
    print("\n=== Combined Analysis ===")

    alice = Player('alice', 2300, True, {"first_kill", "level_10",
                                         "treasure_hunter", "speed_demon"})
    charlie = Player('charlie', 2150, True, {"High_level", "Monster"})
    diana = Player('diana', 2050, False, {"cold_blood", "monster_hunt"})
    bob = Player('bob', 1800, True, {"god_score", "legend", "100_days_strike"})
    list_players = [alice, charlie, diana, bob]
    print(f"Total players: {len(list_players)}")

    set_of_achievements: set = set()
    for player in list_players:
        for achieve in player.achieves:
            set_of_achievements.add(achieve)
    print(f"Total unique achievements: {len(set_of_achievements)}")

    total_score = 0
    for player in list_players:
        total_score += player.score
    print(f"Avarege score: {total_score}")

    top = list_players[0]
    for player in list_players:
        if player.score > top.score:
            top = player
    print(f"Top performace: {top.name}",
          f"({top.score} points, {len(top.achieves)} achievements)")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    list_examples()
    dict_examples()
    set_examples()
    combined_analysis()
