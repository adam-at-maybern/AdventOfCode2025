# part 1
# lines = []  # save all lines
# locations = set()  # horizontal locations of beam for the next line
# for line in open("input.txt", "r"):
#     line = line.rstrip("\n")
#     line_list = []
#     first = True
#     for col, c in enumerate(line):
#         line_list.append(c)
#         if first:
#             if c == "S":
#                 locations.add(col)
#     first = False
#     lines.append(line_list)

# splits = 0
# num_cols = len(lines[0])
# for row in range(2, len(lines) - 1):
#     new_locations = set()
#     for location in (
#         locations
#     ):  # current lines location that will enable use to fill in new_locations
#         if lines[row][location] != "^":
#             new_locations.add(location)
#         else:
#             splits += 1
#             new_locations.add(location + 1)
#             new_locations.add(location - 1)
#     locations = new_locations

# print(splits)


# part 2
from typing import Any

lines = []  # save all lines
queue = []
worlds = 0
for line in open("input.txt", "r"):
    line = line.rstrip("\n")
    line_list = []
    first = True
    for col, c in enumerate(line):
        line_list.append(c)
        if first:
            if c == "S":
                start = (1, col)
    first = False
    lines.append(line_list)

cache = dict[Any, Any]()


def ways_this_one_ends(original_row, original_col):
    worlds = 1
    if (original_row, original_col) in cache:
        print("cache hit")
        return cache[(original_row, original_col)]
    row = original_row
    col = original_col
    follow_up = []
    while row < len(lines) - 1:
        if lines[row + 1][col] == "^":
            follow_up.append((row + 1, col + 1))
            col -= 1
        row += 1
    for follow_up_row, follow_up_col in follow_up:
        worlds += ways_this_one_ends(follow_up_row, follow_up_col)
    cache[(original_row, original_col)] = worlds
    return worlds


print(ways_this_one_ends(start[0], start[1]))
