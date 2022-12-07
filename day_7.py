class Node:
    def __init__(self, size, parent, children, listed, total_size):
        self.file_size = size
        self.parent = parent
        self.children = children
        self.listed = listed
        self.total_size = total_size


def mark_sizes(root):
    if not root.children:
        root.total_size = root.file_size
    else:
        children_sizes = [mark_sizes(child) for child in root.children.values()]
        root.total_size = sum(children_sizes) + root.file_size
    return root.total_size


def sum_directories_leq_100000(root):
    if not root.children:
        if root.total_size <= 100000:
            return root.total_size
        else:
            return 0
    else:
        children_sizes = [sum_directories_leq_100000(child) for child in root.children.values()]
        if root.total_size <= 100000:
            return root.total_size + sum(children_sizes)
        else:
            return sum(children_sizes)


def find_smallest_directory_to_delete(root, smallest, size_to_delete):
    if not root.children:
        if size_to_delete <= root.total_size < smallest:
            return root.total_size
        else:
            # This won't be selected
            return 100000000000
    else:
        children_smallest_sizes = [find_smallest_directory_to_delete(child, smallest, size_to_delete) for child in root.children.values()]
        if root.total_size >= size_to_delete:
            return min(min(children_smallest_sizes), root.total_size)
        else:
            return min(children_smallest_sizes)


def construct_tree():
    root = Node(0, None, {}, False, 0)
    curr_dir = root
    with open("day_7_input.txt") as fp:
        lines = fp.readlines()
        for line in lines:
            chars = line.split()
            if chars[0] == "$":
                if chars[1] == "cd":
                    if chars[2] == "/":
                        curr_dir = root
                    elif chars[2] == "..":
                        curr_dir = curr_dir.parent
                    else:
                        if chars[2] in curr_dir.children.keys():
                            curr_dir = curr_dir.children[chars[2]]
                        else:
                            curr_dir.children[chars[2]] = Node(0, curr_dir, {}, False, 0)
                            curr_dir = curr_dir.children[chars[2]]
            elif chars[0] == "dir":
                if not curr_dir.listed:
                    if chars[1] not in curr_dir.children.keys():
                        curr_dir.children[chars[1]] = Node(0, curr_dir, {}, False, 0)
            else:
                if not curr_dir.listed:
                    curr_dir.file_size += int(chars[0])
    return root


if __name__ == "__main__":
    tree = construct_tree()
    root_size = mark_sizes(tree)
    directories_leq_100000_sum = sum_directories_leq_100000(tree)
    size_to_delete = 30000000 - (70000000 - root_size)
    smallest_directory_to_delete = find_smallest_directory_to_delete(tree, 100000000000, size_to_delete)
    print(f"Sum of directories of size below 100000 = {directories_leq_100000_sum}")
    print(f"Total space taken up = {root_size}")
    print(f"Size needed to free up = {size_to_delete}")
    print(f"Size of directory to delete: {smallest_directory_to_delete}")