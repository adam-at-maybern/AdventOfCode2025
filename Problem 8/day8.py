points = []  # point i initially contains  [[xi, yi, zi], i] with second part of list the circuit it belongs to
circuits = dict()  # circuit number to list of points


def distance_between(pointA, pointB):
    return (
        (pointA[0][0] - pointB[0][0]) ** 2
        + (pointA[0][1] - pointB[0][1]) ** 2
        + (pointA[0][2] - pointB[0][2]) ** 2
    ) ** 0.5


def connect_points(pointA, pointB):
    circuitA_id = pointA[1]
    circuitB_id = pointB[1]

    if circuitA_id == circuitB_id:
        return
    # change all the points in circuitA to circuitB
    # add all the points in circuitB to circuitA
    # delete circuit A
    for point in circuits[circuitA_id]:
        point[1] = circuitB_id
    circuits[circuitB_id].extend(circuits[circuitA_id])
    del circuits[circuitA_id]


i = 0
for line in open("input.txt", "r"):
    line = line.rstrip("\n")
    points.append([[int(x) for x in line.split(",")], i])
    circuits[i] = [points[i]]
    i += 1

num_points = len(points)
distances = []  # (distance, pointA, pointB)
for a in range(num_points):
    for b in range(a + 1, num_points):
        distances.append((distance_between(points[a], points[b]), points[a], points[b]))
distances = sorted(distances)

i = 0
while len(circuits) > 1:
    distance = distances[i]
    connect_points(distance[1], distance[2])
    i += 1

print(distances[i - 1][1][0][0] * distances[i - 1][2][0][0])
