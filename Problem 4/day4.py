def count_neighbors(grid, row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                continue
            count += grid[i][j]
    return count


grid = []
res = 0
for line in open("input.txt", "r"):
    line = line.strip()
    grid.append([1 if c == "@" else 0 for c in line])

new_res = 0
first = True
while new_res != 0 or first:
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    new_res = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                if count_neighbors(grid, row, col) < 4:
                    new_res += 1
                else:
                    new_grid[row][col] = 1
    res += new_res
    grid = new_grid
    first = False
    print(new_res)
print(res)
