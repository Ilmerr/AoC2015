from collections import defaultdict
from itertools import permutations

places = set()
graph = defaultdict(dict)
for line in open("input.txt"):
    src, _, dst, _, dist = line.split()
    places.add(src)
    places.add(dst)
    graph[src][dst] = int(dist)
    graph[dst][src] = int(dist)

distances = []
for perm in permutations(places):
    distances.append(sum(map(lambda i, j: graph[i][j], perm[:-1], perm[1:])))

print(max(distances))
output = open('output2.txt', 'w')
output.write(str(max(distances)))

output.close()