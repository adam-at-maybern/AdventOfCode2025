# part 1
# res = 0
# lines = []
# for line in open("input.txt", "r"):
#     line = line.strip()
#     line = line.split(" ")
#     line = [x for x in line if x != ""]
#     lines.append(line)
# for i in range(len(lines[0])):
#     col_i_res = 0
#     if lines[-1][i] == "*":
#         col_i_res = 1
#         for j in range(len(lines) - 1):
#             col_i_res *= int(lines[j][i])
#     elif lines[-1][i] == "+":
#         for j in range(len(lines) - 1):
#             col_i_res += int(lines[j][i])

#     res += col_i_res

# part 2
res = 0
lines = []
for line in open("input.txt", "r"):
    line = line.rstrip("\n")
    line = [c for c in line]
    lines.append(line)

operator_locations = []
for i, c in enumerate(lines[-1]):
    if c == "*" or c == "+":
        operator_locations.append((c, i))

for i, (operator, location) in enumerate(operator_locations):
    prob_res = 0
    if operator == "*":
        prob_res = 1
        for col in range(
            location,
            operator_locations[i + 1][1] - 1
            if i + 1 < len(operator_locations)
            else len(lines[0]),
        ):
            num = ""
            for row in range(len(lines) - 1):
                num += lines[row][col]
            prob_res *= int(num)
    elif operator == "+":
        prob_res = 0
        for col in range(
            location,
            operator_locations[i + 1][1] - 1
            if i + 1 < len(operator_locations)
            else len(lines[0]),
        ):
            num = ""
            for row in range(len(lines) - 1):
                num += lines[row][col]
            prob_res += int(num)
    res += prob_res

print(res)
