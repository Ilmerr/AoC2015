STRING = open('input.txt').read()
if STRING[-1] == '\n':
    STRING = STRING[:-1]

answer1 = STRING

for i in range(40):
    new = ''
    s = 0
    while s < len(answer1):
        c = answer1[s]
        n = 1
        s += 1
        while s < len(answer1) and answer1[s] == c:
            s += 1
            n += 1
        new += str(n) + str(c)
    answer1 = new

print(len(answer1))

with open('output1.txt', 'w') as f:
    print((len(answer1)), file=f)