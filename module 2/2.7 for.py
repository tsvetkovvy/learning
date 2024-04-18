# Циклы

# while - цикл выполняется, пока высказывание в условии не станет ложным
# for - цикл выполняется, пока в итерируемом объекте есть значения

if __name__ == '__main__':

    # while example
    # is_succeeded = False
    # attempts = 0
    # while attempts < 10 and not is_succeeded:
    #     is_succeeded = retry()
    #     attempts += 1

    # for example
    # for i in range(5):
    #     print(i)

    last_humidity = None
    while last_humidity is None:
        print('Введите влажность (целое число)')
        input_data = input()
        if input_data.isdigit():
            last_humidity = int(input_data)

    workroom_humidity = (42, 46, 39, 47, 53, 58, 52, 53, 48, last_humidity)

    sum_of_humidity = 0
    for humidity in workroom_humidity:
        sum_of_humidity += humidity

    for i in range(1, 6):
        print(sum_of_humidity / len(workroom_humidity))


