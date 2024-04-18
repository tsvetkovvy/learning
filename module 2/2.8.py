# Списки

if __name__ == '__main__':
    my_list = [1, 2, 3]
    my_list.append('four') # Добавить элемент в список
    my_list.extend([5, 6, 7]) # Расширить список другим списком
    # print(my_list) # > [1, 2, 3, 'four', 5, 6, 7]

    #my_list.pop() # Извлечь последний элемент списка
    # print(my_list.pop()) # > 7
    # print(my_list) # > [1, 2, 3, 'four', 5, 6]

    my_list = [1, 2, 3]
    my_list.reverse()
    # print(my_list)

    my_list = [2, 3, 1]
    my_list.sort(reverse=True)
    # print(my_list)

    my_list = [1, 2, 3]
    my_list.clear()
    # print(my_list)

    my_list = [2, 3, 1]
    another_list = my_list.copy()
    another_list.append(4)
    # print (my_list) # > [2, 3, 1]
    # print(another_list) # > [2, 3, 1, 4]

    # Practice
    workroom_humidity = [42, 46, 39, 47, 53, 58, 52, 53, 48]

    while True:
        print('Введите влажность (целое число)')
        input_data = input()
        if input_data.isdigit():
            workroom_humidity.append(int(input_data))
        elif ',' in input_data:
            workroom_humidity.extend(map(int, input_data.split(',')))
        elif input_data == '':
            break
        else:
            print('Валидация не пройдена')

    workroom_humidity.sort()
    print(workroom_humidity)
    outlier = workroom_humidity.pop()
    print(outlier)
    print(workroom_humidity)

    sum_of_humidity = 0
    for humidity in workroom_humidity:
        sum_of_humidity += humidity

    for i in range(1, 6):
        print(sum_of_humidity / len(workroom_humidity))

