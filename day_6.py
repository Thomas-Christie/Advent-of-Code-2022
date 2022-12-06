def find_start_index():
    with open("day_6_input.txt") as fp:
        line = fp.readline()
        i = 0
        duplicate_characters = True
        while duplicate_characters and i < len(line) - 3:
            duplicate_characters = False
            substring = line[i:i+4]
            for j in range(4):
                for k in range(j+1, 4):
                    if substring[j] == substring[k]:
                        duplicate_characters = True
            if not duplicate_characters:
                return i + 4
            else:
                i += 1


def find_message_start_index():
    with open("day_6_input.txt") as fp:
        line = fp.readline()
        i = 0
        duplicate_characters = True
        while duplicate_characters and i < len(line) - 13:
            duplicate_characters = False
            substring = line[i:i+14]
            for j in range(14):
                for k in range(j+1, 14):
                    if substring[j] == substring[k]:
                        duplicate_characters = True
            if not duplicate_characters:
                return i + 14
            else:
                i += 1


if __name__ == "__main__":
    start_index = find_start_index()
    message_start_index = find_message_start_index()
    print(f"Start index: {start_index}")
    print(f"Message start index: {message_start_index}")
