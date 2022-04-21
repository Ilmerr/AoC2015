input_string = open('input.txt').read()
if input_string[-1] == '\n':
    input_string = input_string[:-1]

def is_really_nice(s):
    first = False
    for i in range(len(s) - 3):
        sub = s[i: i + 2]
        if sub in s[i + 2:]:
            first = True
            break
    if not first:
        return False
    second = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            second = True
            break
    return second

count2 = 0
for s in input_string.split('\n'):
    if is_really_nice(s):
        count2 += 1

print(count2)
output = open('output2.txt', 'w')
output.write(str(count2))

output.close()