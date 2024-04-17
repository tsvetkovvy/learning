# Переменные

if __name__ == '__main__':
    # payment_amount = 3000
    # payment_amount += 1000  # Переприсовение значения переменной
    #
    # print(payment_amount * 0.1)  # Чаевые
    # print(payment_amount)

    # Practice
    mb = 1024
    containers_quantity = 68796
    container_size = 30  # Mb
    node_ram = 16  # Gb
    data_centers_quantity = (containers_quantity / (4 * 117 * 21))
    print(data_centers_quantity)  # Quantity of Data Centres
    free = ((node_ram * mb * 21 * data_centers_quantity) - (container_size * containers_quantity))
    print(free)  # Free ROM in infrastructure (Mb)
    free_gb = free // mb
    free_mb = free % mb
    print('Свободно', free_gb, 'гигабайт', free_mb, 'мегабайт')  # Free ROM

