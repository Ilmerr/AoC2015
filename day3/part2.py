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


def part2():
    santa, robo = [0, 0], [0, 0]
    result = {(0, 0)}
    for i, d in enumerate(open('input.txt').read()):
        if i % 2 == 0:
            santa = next_house(santa, d)
            result.add(tuple(santa))
        else:
            robo = next_house(robo, d)
            result.add(tuple(robo))
    print(len(result))
    with open("output2.txt", "w") as f:
        print(len(result), file=f)

if __name__ == '__main__':
    part2()
