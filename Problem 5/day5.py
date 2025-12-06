def merge_and_sort(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


def is_in_intervals(num: int, intervals: list[list[int]]):
    for interval in intervals:
        if interval[0] <= num <= interval[1]:
            return True
    return False


interval_building = True
intervals = []
res = 0
for line in open("input.txt", "r"):
    line = line.strip()
    if interval_building and len(line) < 1:
        interval_building = False
        continue
    if interval_building:
        intervals.append([int(x) for x in line.split("-")])
    else:
        print(sum([b - a + 1 for a, b in merge_and_sort(intervals)]))
        break
