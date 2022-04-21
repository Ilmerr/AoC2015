def next_house(loc, d):
    result = loc[:]
    if d == '<':
        result[0] += -1
    elif d == '>':
        result[0] += 1
    elif d == '^':
        result[1] += 1
    elif d == 'v':
        result[1] += -1
    return result

def part1():
    loc = [0, 0]
    result = {(0, 0)}
    for d in open('input.txt').read():
        loc = next_house(loc, d)
        result.add(tuple(loc))
    print (len(result))
    with open("output1.txt", "w") as f:
        print(len(result), file=f)

if __name__ == '__main__':
    part1()
