c = 0
d = 0

with open('input.txt') as f:
    for l in f:
        data = l.strip()
        literal = len(data)
        double = 2
        for ch in data:
            if ch in ['"', '\\']:
                double += 2
            else:
                double += 1

        c += literal
        d += double

print(d - c)
output = open('output2.txt', 'w')
output.write(str(d-c))

output.close()