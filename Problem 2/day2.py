def is_valid(n):
    for sublength in range(1, len(n) // 2 + 1):
        if len(n) % sublength:
            continue
        if n[0:sublength] * (len(n) // sublength) == n:
            return False
    return True


res = 0
for line in open("input.txt", "r"):
    for pair in line.strip().split(","):
        a, b = pair.split("-")
        for i in range(int(a), int(b) + 1):
            if not is_valid(str(i)):
                res += i
print(res)
