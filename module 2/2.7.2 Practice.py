if __name__ == '__main__':
    rps_values = (
    5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602', 14116,
    '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203', 13303, '7330', 7186,
    '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817, '16187', '6381', 8409, '5177', 17357,
    '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850, '12791',
    11288)

    corrected_rps_values = sorted(int(value) for value in rps_values)
    # print(corrected_rps_values)

    quotient, remainder = divmod(len(corrected_rps_values), 2)
    median = corrected_rps_values[quotient] if remainder else sum(corrected_rps_values[quotient - 1:quotient + 1]) / 2
    print(median)

    sum_of_rps = 0
    for i in corrected_rps_values:
        sum_of_rps += i
    mean_rps = sum_of_rps / len(corrected_rps_values)
    print(mean_rps)

    direction = mean_rps/median - 1
    print(direction)

    if direction > 0.3:
        direction_string = 'Снижения'
    elif direction < -0.3:
        direction_string = 'Скачки'
    else:
        direction_string = 'Стабильная'

    print(f'{mean_rps//1:.0f} {median:.0f} {direction_string}')
