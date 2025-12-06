res = 0


def get_nth_digit(n, line):
    highest, highest_index = 0, 0
    for i in range(len(line) - (n)):
        if int(line[i]) > highest:
            highest = int(line[i])
            highest_index = i
    return highest, highest_index


for line in open("input.txt", "r"):
    line = line.strip()
    highest_index = 0
    for n in range(11, -1, -1):
        highest, idx = get_nth_digit(n, line[highest_index:])
        highest_index = idx + highest_index + 1
        res += highest * 10**n

print(res)
