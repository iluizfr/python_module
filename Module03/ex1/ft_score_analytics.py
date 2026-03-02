import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if (len(sys.argv) < 2):
        print(f"No scores provided. Usage: {sys.argv[0]} <score1> <score2> ..")
    else:
        try:
            total_players = len(sys.argv) - 1
            total_score = 0
            integer_list = []
            i = 1

            for arg in sys.argv:
                if (i < len(sys.argv)):
                    total_score += int(sys.argv[i])
                    integer_list += [sys.argv[i]]
                    i += 1

            avarege_score = total_score / total_players
            high_score = max(integer_list)
            low_score = min(integer_list)
            score_range = int(high_score) - int(low_score)

            print(f"Score processed: {integer_list}")
            print(f"Total players: {total_players}")
            print(f"Total score: {total_score}")
            print(f"Avarege score: {avarege_score}")
            print(f"High score: {high_score}")
            print(f"Low score: {low_score}")
            print(f"Score range: {score_range}\n")
        except ValueError:
            print("Ops, only numbers for scores..\n")
            sys.exit(1)
