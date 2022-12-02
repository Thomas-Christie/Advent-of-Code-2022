def count_max_calories():
    max_calories = 0
    with open("day_1_input.txt") as fp:
        lines = fp.readlines()
        curr_calories = 0
        for line in lines:
            if line.strip() == "":
                if curr_calories > max_calories:
                    max_calories = curr_calories
                curr_calories = 0
            else:
                curr_calories += int(line.strip())
    return max_calories


def count_top_three_calories():
    first_calories = 0
    second_calories = 0
    third_calories = 0
    with open("day_1_input.txt") as fp:
        lines = fp.readlines()
        curr_calories = 0
        for line in lines:
            if line.strip() == "":
                if curr_calories >= first_calories:
                    third_calories = second_calories
                    second_calories = first_calories
                    first_calories = curr_calories
                elif curr_calories >= second_calories:
                    third_calories = second_calories
                    second_calories = curr_calories
                elif curr_calories > third_calories:
                    third_calories = curr_calories
                curr_calories = 0
            else:
                curr_calories += int(line.strip())
    return first_calories + second_calories + third_calories


if __name__ == "__main__":
    print(f"Max Calories: {count_max_calories()}")
    print(f"Sum of Top Three Calories: {count_top_three_calories()}")