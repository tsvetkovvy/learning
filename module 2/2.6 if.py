# Условный оператор

if __name__ == '__main__':

    # TODO: нас интересуют 2 вендора: Brrr и SMF
    # TODO: размер входной двери 210х90 мм
    # TODO: размер панорамного окна 170х320 мм
    # TODO: холодильник наклонять нельзя

    vendor = input()  # заведомо знаем, что нужно вводить определенных вендоров
    fridge_height = int(input())  # заведомо знаем, что нужно вводить число (без доп. проверок)
    fridge_width = int(input())  # заведомо знаем, что нужно вводить число (без доп. проверок)

    # Option 1
    # if vendor in ('Brrr', 'SMF'):  # если указан верный вендор
    #     if fridge_height <= 210 and fridge_width <= 90:  # если проходит в дверь
    #         print('Подходит')
    #     elif fridge_height <= 170 and fridge_width <= 320:
    #         print('Подходит')
    #     else:
    #         print('Не подходит')
    # else:
    #     print('Не подходит')

    # Option 2
    # if vendor in ('Brrr', 'SMF') and ((fridge_height <= 210 and fridge_width <= 90) or (fridge_height <= 170 and fridge_width <= 320)):
    #     print('Подходит')
    # else:
    #     print('Не подходит')

    # Option 3
    # is_pass_through_door = fridge_height <= 210 and fridge_width <= 90
    # is_pass_through_window = (fridge_height <= 170 and fridge_width <= 320)
    # if vendor in ('Brrr', 'SMF') and (is_pass_through_door or is_pass_through_window):
    #     print('Подходит')
    # else:
    #     print('Не подходит')


    # Practice
