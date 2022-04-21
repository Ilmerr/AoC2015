import re

grid = [[False for x in range(1000)] for x in range(1000)]
tot_lights_on = 0

with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        m = re.search('([a-z])\s(\d+),(\d+)[a-z\s]+(\d+),(\d+)', line)

        action = m.group(1)
        x1 = int(m.group(2))
        y1 = int(m.group(3))
        x2 = int(m.group(4))
        y2 = int(m.group(5))

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                prev = grid[x][y]

                if 'n' == action:
                    if not prev:
                        tot_lights_on += 1
                    grid[x][y] = True
                elif 'f' == action:
                    if prev:
                        tot_lights_on -= 1
                    grid[x][y] = False
                elif 'e' == action:
                    tot_lights_on = tot_lights_on - 1 if prev else tot_lights_on + 1
                    grid[x][y] = not prev

print(tot_lights_on)
output = open('output1.txt', 'w')
output.write(str(tot_lights_on))

output.close()