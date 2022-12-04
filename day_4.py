def number_of_inclusive_pairs():
    with open("day_4_input.txt") as fp:
        lines = fp.readlines()
        number = 0
        for line in lines:
            first_elf = line.split(',')[0]
            second_elf = line.split(',')[1]
            first_elf_lower = int(first_elf.split('-')[0])
            first_elf_upper = int(first_elf.split('-')[1])
            second_elf_lower = int(second_elf.split('-')[0])
            second_elf_upper = int(second_elf.split('-')[1])
            if first_elf_lower <= second_elf_lower and first_elf_upper >= second_elf_upper:
                number += 1
            elif first_elf_lower >= second_elf_lower and first_elf_upper <= second_elf_upper:
                number += 1
    return number


def number_of_overlap_pairs():
    with open("day_4_input.txt") as fp:
        lines = fp.readlines()
        number = 0
        for line in lines:
            first_elf = line.split(',')[0]
            second_elf = line.split(',')[1]
            first_elf_lower = int(first_elf.split('-')[0])
            first_elf_upper = int(first_elf.split('-')[1])
            second_elf_lower = int(second_elf.split('-')[0])
            second_elf_upper = int(second_elf.split('-')[1])
            if not first_elf_upper < second_elf_lower and not second_elf_upper < first_elf_lower:
                number += 1
    return number


if __name__ == "__main__":
    total_inclusive_pairs = number_of_inclusive_pairs()
    overlapping_pairs = number_of_overlap_pairs()
    print(f"Total number of inclusive pairs: {total_inclusive_pairs}")
    print(f"Total number of overlapping pairs: {overlapping_pairs}")
