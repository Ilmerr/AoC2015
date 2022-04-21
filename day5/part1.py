input_string = open('input.txt').read()
if input_string[-1] == '\n':
    input_string = input_string[:-1]

def is_nice(s):
    vowels = 0
    for c in s:
        if c in 'aeiou':
            vowels += 1
        if vowels >= 3:
            break
    if vowels < 3:
        return False
    repeat = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeat = True
            break
    if not repeat:
        return False
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return False
    return True

count1 = 0

for s in input_string.split('\n'):
    if is_nice(s):
        count1 += 1

print(count1)
output = open('output1.txt', 'w')
output.write(str(count1))

output.close()
