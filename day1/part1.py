input_string = 'input.txt'

with open(input_string, 'r') as input_file:
    for line in input_file:
        answer = str(len(line.split('('))-len((line.split(')'))))
        print(answer)

with open("output1.txt", "w") as f:
    print(answer, file=f)
