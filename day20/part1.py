def sumer(n):
    SUM = 1
    for i in range(2, 50):
        p = i
        while (n % i == 0):
            n = n // i
            p *= i
        SUM *= (p - 1) // (i - 1)
    return SUM


with open('input.txt', 'r') as INPUT:
    house = int(INPUT.readline()) // 10

presents = 0
counter = 0
while presents < house:
    counter += 1
    presents = sumer(counter)

print('Дом #', counter, ': ', presents, ' подарков', sep='')

with open('output1.txt', 'w') as OUTPUT:
    OUTPUT.write(str(counter))