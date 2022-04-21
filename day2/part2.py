with open('input.txt') as f:
    lines = f.readlines()

total2 = 0

for line in lines:
    l, w, h = map(int, line.split('x'))
    total2 += min(l, w, h) * 2 + sorted([l, w, h])[1] * 2 + (l * w * h)

print(total2)
with open("output2.txt", "w") as f:
    print(total2, file=f)