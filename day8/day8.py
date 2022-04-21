import re

lines = open("day8_input.txt").readlines()
p1 = 0
for line in lines:
    p1 += 2
    p1 += len(re.findall("\\\[\"\\\]", line))
    p1 += 3 * len(re.findall("\\\[x][0-9a-f]{2}", line))
print(p1 )

p2 = 0
for line in lines:
    p2 +=4
    p2 += 2 * len(re.findall("\\\[\"\\\]", line))
    p2 += len(re.findall("\\\[x][0-9a-f]{2}", line))
print(p2)