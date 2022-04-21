with open('input.txt') as f:
    lines = f.readlines()

total1 = 0

for line in lines:
    l, w, h = map(int, line.split('x'))
    total1 += (2 * l * w + 2 * w * h + 2 * h * l) + min(l * w, w * h, h * l)

print(total1)
with open("output1.txt", "w") as f:
    print(total1, file=f)