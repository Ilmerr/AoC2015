import operator

input_string = 'input.txt'

floor = 0
char_count = 0
in_basement = False

with open(input_string, 'r') as input_file:
    for line in input_file:
        for char in line:
            if operator.eq('(',char):
                floor += 1
            elif operator.eq(')',char):
                floor -= 1
            else:
                print('invalid input')
            char_count += 1
            if(floor < 0):
                if not in_basement:
                    in_basement = True
                    print(str(char_count))
                    with open("output2.txt", "w") as f:
                        print(str(char_count), file=f)


input_file.close()