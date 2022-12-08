import numpy as np


def mark_visible_from_left(trees, visibility):
    for row in range(len(trees)):
        max_height = -1
        for col in range(len(trees[0])):
            tree_height = trees[row][col]
            if tree_height > max_height:
                max_height = tree_height
                visibility[row][col] = 1


def mark_visible_from_right(trees, visibility):
    for row in range(len(trees)):
        max_height = -1
        for col in range(len(trees[0]) - 1, -1, -1):
            tree_height = trees[row][col]
            if tree_height > max_height:
                max_height = tree_height
                visibility[row][col] = 1


def mark_visible_from_top(trees, visibility):
    for col in range(len(trees[0])):
        max_height = -1
        for row in range(len(trees)):
            tree_height = trees[row][col]
            if tree_height > max_height:
                max_height = tree_height
                visibility[row][col] = 1


def mark_visible_from_bottom(trees, visibility):
    for col in range(len(trees[0])):
        max_height = -1
        for row in range(len(trees) - 1, -1, -1):
            tree_height = trees[row][col]
            if tree_height > max_height:
                max_height = tree_height
                visibility[row][col] = 1


def parse_input():
    with open("day_8_input.txt") as fp:
        lines = fp.readlines()
        tree_heights = []
        for line in lines:
            heights = list(map(int, list(line)[:-1]))
            tree_heights.append(heights)
    return tree_heights


def number_of_visible_trees():
    tree_heights = parse_input()
    visibility = [[0 for _ in range(len(tree_heights[0]))] for _ in range(len(tree_heights))]
    mark_visible_from_left(tree_heights, visibility)
    mark_visible_from_right(tree_heights, visibility)
    mark_visible_from_top(tree_heights, visibility)
    mark_visible_from_bottom(tree_heights, visibility)
    return np.sum(visibility)


def num_visible_to_left(tree_heights, row, col):
    tree_height = tree_heights[row][col]
    i = 0
    while col - i - 1 >= 0:
        i += 1
        if tree_heights[row][col - i] >= tree_height:
            break
    return i


def num_visible_to_right(tree_heights, row, col):
    tree_height = tree_heights[row][col]
    i = 0
    while col + i + 1 < len(tree_heights[0]):
        i += 1
        if tree_heights[row][col + i] >= tree_height:
            break
    return i


def num_visible_above(tree_heights, row, col):
    tree_height = tree_heights[row][col]
    i = 0
    while row - i - 1 >= 0:
        i += 1
        if tree_heights[row - i][col] >= tree_height:
            break
    return i


def num_visible_below(tree_heights, row, col):
    tree_height = tree_heights[row][col]
    i = 0
    while row + i + 1 < len(tree_heights):
        i += 1
        if tree_heights[row + i][col] >= tree_height:
            break
    return i


def max_scenic_score():
    tree_heights = parse_input()
    max_score = 0
    for row in range(len(tree_heights)):
        for col in range(len(tree_heights[0])):
            left_score = num_visible_to_left(tree_heights, row, col)
            right_score = num_visible_to_right(tree_heights, row, col)
            above_score = num_visible_above(tree_heights, row, col)
            below_score = num_visible_below(tree_heights, row, col)
            scenic_score = left_score * right_score * above_score * below_score
            if scenic_score > max_score:
                max_score = scenic_score
                print(f"Row = {row}, Col = {col}, Right = {right_score}, Left = {left_score}")
    return max_score


if __name__ == "__main__":
    num_visible_trees = number_of_visible_trees()
    max_score = max_scenic_score()
    print(f"Number of visible trees = {num_visible_trees}")
    print(f"Max scenic score = {max_score}")
