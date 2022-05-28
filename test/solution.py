with open('input.txt') as f:
    # Идея заключается в том, что марсоход движется между точками, соторые лежат на пресечении двух из трёх основных окружностей
    data = f.readlines()
    position = 0 # Задаёт положение марсохода на сфере
    vector = 3 # Значение этого вектора задаёт по каким окружностям будет происходить движение
    movement = [[[0, 1, 2, 3], [0, 4, 2, 5], [0, 3, 2, 1], [0, 5, 2, 4]],# Все возможные варианты передвижений
                [[1, 2, 3, 0], [1, 4, 3, 5], [1, 0, 3, 2], [1, 5, 3, 4]],
                [[2, 4, 0, 5], [2, 5, 0, 4], [2, 1, 0, 3], [2, 3, 0, 1]],
                [[3, 2, 1, 0], [3, 0, 1, 2], [3, 4, 1, 5], [3, 5, 1, 4]],
                [[4, 1, 5, 3], [4, 3, 5, 1], [4, 0, 5, 2], [4, 2, 5, 0]],
                [[5, 2, 4, 0], [5, 0, 4, 2], [5, 1, 4, 3], [5, 3, 4, 1]]]

    orientation = [[1, 4, 3, 5], [2, 4, 0, 5], [3, 4, 1, 5], [5, 0, 4, 2], [1, 2, 3, 0], [1, 0, 3, 2]] # Определяет точки,
                                                                    # с которыми изначаельнаая точка может соединятся вектором.
                                                                    # Вектором соединяется изначальная и противоположная точки
    for i in range(len(data)):
        local_data = data[i]
        local_data = local_data.split()
        if local_data[0] == 'FORWARD': # Осуществляем передвижение
            for i in range(len(movement[position])):
                if movement[position][i][3] == vector: # Выбираем подходящий вариант передвижения,
                                                        # 3 указывает на вектор, с которым соединяется точка
                    atribut = i # Вспомогательный атрибут
                    break
            circle = movement[position][atribut] # Подходящий вариант передвижения
            for i in range(int(local_data[1])): # Само перемещение
                circle = [circle[1], circle[2], circle[3], circle[0]] # Передвижение осуществляем за счёт смещения элементов массива
                position = circle[0]
                vector = circle[3]

        elif local_data[0] == 'RIGHT': # В этом блоке задаётся поворот направо
            parametr = 0 # Вспомогательный параметр, проверяет выполнение if
            for j in range(len(orientation[position]) - 1): # Выбираем подходящее значение вектора после поворота
                                                            # ,проверяем первые 3
                if orientation[position][j] == vector: # Если верно, то новым вектором будет следующее значение при повороте
                    print(orientation[position][j], vector)
                    vector = orientation[position][j + 1]
                    parametr += 1
            if parametr == 0: # Если подходящее значение вектора не нашлось, то берём тот элемент, который не рассматривали ранее
                vector = orientation[position][0]

        elif local_data[0] == 'LEFT': # Аналогично повороту налево, только из рассмотрения исключаем первое значение
            parametr = 0
            for i in range(1, len(orientation[position])):
                if orientation[position][i] == vector:
                    vector = orientation[position][i - 1]
                    parametr += 1
            if parametr == 0:
                vector = orientation[position][3]
        else:
            break
with open('output.txt', 'w') as h:
    h.write(str(position))