a = 0
b = 0

with open('input.txt') as f:
    for l in f:
        data = l.strip()
        literal = len(data)
        memory = 0
        flag = 0
        for ch in data[1:-1]:
            if flag == 0 and ch == '\\':
                flag = 1
            elif flag == 1 and ch == 'x':
                flag = 2
            elif flag == 2:
                flag = 3
            elif flag == 3:
                flag = 0
                memory += 1
            elif flag == 1:
                flag = 0
                memory += 1
            else:
                memory += 1

        b += literal
        a += memory

print(b - a)
output = open('output1.txt', 'w')
output.write(str(b-a))

output.close()

