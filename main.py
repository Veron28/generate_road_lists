from excel_generation import excel_generation


excel_name_file = input('Введите полное назнание файла с транзакциями: ')

for i in range(1):

    print('Первая машина')
    gas_consumption = float(input('Введите расход первой машины '))
    gas_leftover_by_start_of_month = float(input('Введите остаток бензина первой машины на начало месяца '))
    gas_leftover_by_end_of_month = float(input('Введите желаемый остаток бензина первой машины на конец месяца '))
    tank_capacity = float(input('Введите вместимость первой машины '))
    odometer_reading = float(input('Введите показания одометра на начало месяца первой машины '))
    print('Идет генерация excel')
    excel_generation(gas_consumption, gas_leftover_by_start_of_month, gas_leftover_by_end_of_month, tank_capacity, excel_name_file, 1, odometer_reading)

    print('Генерация завершена')

    print('Вторая машина')
    gas_consumption = float(input('Введите расход второй машины '))
    gas_leftover_by_start_of_month = float(input('Введите остаток бензина второй машины на начало месяца '))
    gas_leftover_by_end_of_month = float(input('Введите желаемый остаток бензина второй машины на конец месяца '))
    tank_capacity = float(input('Введите вместимость второй машины '))
    odometer_reading = float(input('Введите показания одометра на начало месяца второй машины '))
    print('Идет генерация excel')
    excel_generation(gas_consumption, gas_leftover_by_start_of_month, gas_leftover_by_end_of_month, tank_capacity,
                     excel_name_file, 2, odometer_reading)

    print('Генерация завершена')


gas_consumption = 12.64
gas_leftover_by_start_of_month = 5
gas_leftover_by_end_of_month = 10

tank_capacity = 50
excel_name_file = 'TransactionsTableАпрель.xls'
car_number = 2
odometer_reading = 100000