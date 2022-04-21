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

answer2 = answer1

for i in range(10):
    new = ''
    s = 0
    while s < len(answer2):
        c = answer2[s]
        n = 1
        s += 1
        while s < len(answer2) and answer2[s] == c:
            s += 1
            n += 1
        new += str(n) + str(c)
    answer2 = new

print(len(answer2))

with open('output2.txt', 'w') as f:
    print((len(answer2)), file=f)