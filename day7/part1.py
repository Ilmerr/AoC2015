functions = {}
functions["AND"] = lambda x, y: x & y
functions["OR"] = lambda x, y: x | y
functions["NOT"] = lambda x, y: ~y
functions["RSHIFT"] = lambda x, y: x >> y
functions["LSHIFT"] = lambda x, y: x << y


def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def solve(knot, knots):
    for line in knots:
        if line[0] == knot:
            if line[2] != -1:
                return line[2]
            args = line[1].split(" ")
            if len(args) == 1:
                if not isInt(args[0]):
                    line[2] = int(solve(args[0], knots))
                else:
                    line[2] = int(args[0])
                return line[2]
            if not isInt(args[0]) and len(args) == 3:
                args[0] = int(solve(args[0], knots))
            elif len(args) == 3:
                args[0] = int(args[0])
            if not isInt(args[-1]):
                args[-1] = int(solve(args[-1], knots))
            else:
                args[-1] = int(args[-1])
            line[2] = functions[args[-2]](args[0], args[-1])
            return line[2]
    return -1


lines = open("input.txt", "r").read().split("\n")
knots = []
for line in lines:
    lineSplit = line.split("->")
    knot = [lineSplit[1].strip(), lineSplit[0].strip(), -1]
    knots.append(knot)
    knots = sorted(knots)

answer = solve("a", knots)
print(answer)
output = open('output1.txt', 'w')
output.write(str(answer))

output.close()
