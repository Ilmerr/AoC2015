from random import shuffle, randint
from re import split as spl
import time
import sys

sys.setrecursionlimit(10000)

with open('input.txt', 'r') as INPUT:
    array = []
    for line in INPUT:
        line = line.strip()
        if '=>' in line:
            line = line.replace(' =>', '')
            line = line.split(' ')
            array.append(line)
        else:
            main_molecule = line
################################


# Сортировка#
for element in array:
    counter = 0
    for el in element[1]:
        if el.isupper() == True:  # Считаем кол-во заглавных символов
            counter += 1
    element.append(counter)
array.sort(key=lambda x: x[2], reverse=True)  # Сортируем список по убыванию заглавных символов

for element in array:  # Избавляемся от ненужных последних значений кол-ва заглавных символов
    element.remove(element[-1])


############


# Главная функция#
def minimize(molecule, array, last=[], switcher=0):
    if switcher == 1:
        last1 = last.copy()
        x = last1[-1][1]
    elif switcher == 0:
        x = 0
    else:
        print('so intresting...')
    for i in range(x,
                   len(array)):
        if switcher == 1:
            switcher = 0
            last.remove(last[-1])
            continue
        if array[i][1] in molecule:

            last.append([molecule, i])

            n = molecule.find(array[i][1])
            molecule = molecule[:n] + array[i][0] + molecule[
                                                    n + len(array[i][1]):]
            print(molecule)

            return minimize(molecule, array, last)

    if molecule == 'e':
        return len(last)

    switcher = 1
    return minimize(last[-1][0], array, last, switcher)

a = minimize(main_molecule, array)
print(a)