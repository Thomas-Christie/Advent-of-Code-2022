def count_score():
    with open("day_2_input.txt") as fp:
        lines = fp.readlines()
        score = 0
        for line in lines:
            opponent = line[0]
            player = line[2]
            if player == "X":
                score += 1
                if opponent == "A":
                    score += 3
                elif opponent == "C":
                    score += 6
            elif player == "Y":
                score += 2
                if opponent == "B":
                    score += 3
                elif opponent == "A":
                    score += 6
            else:
                score += 3
                if opponent == "C":
                    score += 3
                elif opponent == "B":
                    score += 6
        return score


# A = Rock = 1 Point
# B = Paper = 2 Points
# C = Scissors = 3 Point
# X = Lose
# Y = Draw
# Z = Win
def count_modified_score():
    with open("day_2_input.txt") as fp:
        lines = fp.readlines()
        score = 0
        for line in lines:
            opponent = line[0]
            player = line[2]
            if player == "X":
                if opponent == "A":
                    score += 3
                elif opponent == "B":
                    score += 1
                else:
                    score += 2
            elif player == "Y":
                score += 3
                if opponent == "A":
                    score += 1
                elif opponent == "B":
                    score += 2
                else:
                    score += 3
            else:
                score += 6
                if opponent == "A":
                    score += 2
                elif opponent == "B":
                    score += 3
                else:
                    score += 1
        return score


if __name__ == "__main__":
    print(f"Total Score: {count_score()}")
    print(f"Total Score with Modified Rules: {count_modified_score()}")
