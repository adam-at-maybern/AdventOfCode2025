original_points = []
for line in open("input.txt", "r"):
    original_points.append([int(x) for x in line.rstrip("\n").split(",")])

# Build coordinate compression mappings
unique_x = sorted(set(p[0] for p in original_points))
unique_y = sorted(set(p[1] for p in original_points))
x_to_idx = {x: i for i, x in enumerate(unique_x)}
y_to_idx = {y: i for i, y in enumerate(unique_y)}

# Convert to compressed coordinates (+1 offset to leave margin for flood fill)
points = [[x_to_idx[p[0]] + 1, y_to_idx[p[1]] + 1] for p in original_points]

# +2 for the margin on each side
MAX_SIZE = max(len(unique_x), len(unique_y)) + 2


def area(point1, point2, filled_in, orig_point1, orig_point2):
    for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
        for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
            if not filled_in[x][y]:
                return 0
    # Use original coordinates for actual area
    return (abs(orig_point1[0] - orig_point2[0]) + 1) * (
        abs(orig_point1[1] - orig_point2[1]) + 1
    )


def fill_in_up_to_border(border_points, filled_in):
    visited = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
    queue = [[0, 0]]
    while queue:
        point = queue.pop(0)
        if visited[point[0]][point[1]]:
            continue
        visited[point[0]][point[1]] = 1
        filled_in[point[0]][point[1]] = 1
        for x in range(point[0] - 1, point[0] + 2):
            for y in range(point[1] - 1, point[1] + 2):
                if x == point[0] and y == point[1]:
                    continue
                if 0 <= x < MAX_SIZE and 0 <= y < MAX_SIZE and not border_points[x][y]:
                    queue.append([x, y])
    for i in range(MAX_SIZE):
        for j in range(MAX_SIZE):
            filled_in[i][j] = False if filled_in[i][j] else True


def fill_border_piece(start_point, end_point, borders):
    if start_point[0] == end_point[0]:
        for y in range(
            min(start_point[1], end_point[1]), max(start_point[1], end_point[1]) + 1
        ):
            borders[start_point[0]][y] = True
    elif start_point[1] == end_point[1]:
        for x in range(
            min(start_point[0], end_point[0]), max(start_point[0], end_point[0]) + 1
        ):
            borders[x][start_point[1]] = True


border = [[False] * MAX_SIZE for _ in range(MAX_SIZE)]
filled_in = [[False] * MAX_SIZE for _ in range(MAX_SIZE)]
max_area = 0
for i in range(len(points)):
    if i > 0:
        print("filling border piece")
        fill_border_piece(points[i - 1], points[i], border)
fill_border_piece(points[-1], points[0], border)
fill_in_up_to_border(border, filled_in)
print("filled in")
for i, point1 in enumerate(points):
    for j, point2 in enumerate(points[i + 1 :], start=i + 1):
        max_area = max(
            max_area,
            area(point1, point2, filled_in, original_points[i], original_points[j]),
        )
print(max_area)
