if __name__ == '__main__':
    rps_values = [5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602', 14116,
        '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203', 13303, '7330',
        7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817, '16187', '6381', 8409, '5177', 17357,
        '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850,
        '12791', 11288]

    corrected_rps_values = sorted(int(value) for value in rps_values)
    print(corrected_rps_values)

    while True:
        print('Введите значения rps (целое число)')
        rps_input = input()
        if rps_input.isdigit():
            corrected_rps_values.append(int(rps_input))
        elif ';' in rps_input:
            corrected_rps_values.extend(map(int, rps_input.split(';')))
        elif ',' in rps_input:
            count_of_inputs = len(rps_input.split(','))
            corrected_rps_values.extend(map(int, rps_input.split(',')))
            corrected_rps_values = corrected_rps_values[-count_of_inputs:]
            print(corrected_rps_values)
            break
        elif rps_input == '':
            break
        else:
            print('Валидация не пройдена')

    quotient, remainder = divmod(len(corrected_rps_values), 2)
    median = corrected_rps_values[quotient] if remainder else sum(corrected_rps_values[quotient - 1:quotient + 1]) / 2

    sum_of_rps = 0
    for i in corrected_rps_values:
        sum_of_rps += i
    mean_rps = sum_of_rps / len(corrected_rps_values)

    direction = mean_rps / median - 1
    # print(direction)

    if direction > 0.25:
        direction_string = 'Происходят снижения'
    elif direction < -0.25:
        direction_string = 'Происходят скачки'
    else:
        direction_string = 'Нагрузка стабильна'

    print(f'{mean_rps // 1:.0f} {median:.0f} {direction_string}')
