loc = 50
res = 0
with open("input.txt", "r") as file:
    for line in file:
        go_left = line.strip()[0] == "L"
        count = (int)(line.strip()[1:])
        res += count // 100
        count %= 100
        if go_left:
            if 0 < loc <= count:
                res += 1
            loc = (loc - count) % 100
        else:
            if loc + count >= 100:
                res += 1
            loc = (loc + count) % 100

print(res)
