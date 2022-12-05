import re


def parse_stacks(num_stacks=9):
    with open("day_5_input.txt") as fp:
        lines = fp.readlines()
        stacks = ["" for _ in range(num_stacks)]
        for line in lines:
            if line[0] != '[':
                break
            else:
                for i in range(num_stacks):
                    new_item = line[4*i + 1]
                    if new_item != ' ':
                        stacks[i] = stacks[i] + new_item
    return stacks


def rearrange_stacks():
    stacks = parse_stacks(num_stacks=9)
    with open("day_5_input.txt") as fp:
        lines = fp.readlines()
        for line in lines:
            if line[0] == 'm':
                vals = re.split('\D+', line)
                del vals[0]
                del vals[-1]
                source = int(vals[1])
                dest = int(vals[2])
                num = int(vals[0])
                for _ in range(num):
                    item = stacks[source - 1][0]
                    stacks[source - 1] = stacks[source - 1][1:]
                    stacks[dest - 1] = item + stacks[dest - 1]
    return stacks


def rearrange_stacks_part_two():
    stacks = parse_stacks(num_stacks=9)
    with open("day_5_input.txt") as fp:
        lines = fp.readlines()
        for line in lines:
            if line[0] == 'm':
                vals = re.split('\D+', line)
                del vals[0]
                del vals[-1]
                source = int(vals[1])
                dest = int(vals[2])
                num = int(vals[0])
                items = stacks[source - 1][0:num]
                stacks[source - 1] = stacks[source - 1][num:]
                stacks[dest - 1] = items + stacks[dest - 1]
    return stacks


if __name__ == "__main__":
    stacks_one = rearrange_stacks()
    stacks_two = rearrange_stacks_part_two()
    top_items_one = ""
    top_items_two = ""
    for stack in stacks_one:
        top_items_one += stack[0]

    for stack in stacks_two:
        top_items_two += stack[0]

    print(f"Top items using first rearrangement rules: {top_items_one}")
    print(f"Top items using second rearrangement rules: {top_items_two}")
