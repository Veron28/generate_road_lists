import pandas as pd
import calendar
from random import random



def transaction(df, gas_consumption, gas_leftover_by_start_of_month, gas_leftover_by_end_of_month,tank_capacity, car):
    df = df[df['Ед. изм.'] == 'л']
    if car == 1:
        dfCarOne = df[(df['Карта'] == 3005541161)]  # Машина 1
    else:
        dfCarOne = df[(df['Карта'] == 3005541160) | (df['Карта'] == 3005541162)]  # Машина 2
    dfCarOne = dfCarOne[['Дата трн.', 'Услуга', 'Кол-во']][::-1].reset_index(drop=True)

    days_in_month = calendar.monthrange(dfCarOne['Дата трн.'][0].year, dfCarOne['Дата трн.'][0].month)
    list_of_gas_station_days = dfCarOne['Дата трн.'].apply(lambda x: x.day).value_counts().sort_index().index.to_list()

    list_of_gas_station = [sum(dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)]['Кол-во']) for i in list_of_gas_station_days]
    last_day = 1
    range_of_days = []
    gas_leftover = []
    gas_capacity = gas_leftover_by_start_of_month
    gas_capacity_list = []
    # Range of month days

    if list_of_gas_station_days.count(1) == 0:
        if dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])].shape[0] > 1:
            range_of_days.append([last_day, list_of_gas_station_days[0] - 1])
            range_of_days.append([list_of_gas_station_days[0], list_of_gas_station_days[0]])
            last_day = list_of_gas_station_days[0] + 1
        elif dfCarOne['Дата трн.'][list_of_gas_station_days[0]].hour < 12:
            range_of_days.append([last_day, list_of_gas_station_days[0] - 1])
            last_day = list_of_gas_station_days[0]
        else:
            range_of_days.append([last_day, list_of_gas_station_days[0]])
            last_day = list_of_gas_station_days[0] + 1
    for i in range(last_day, days_in_month[1] + 1):
        if list_of_gas_station_days.count(i) != 0:
            if dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)].shape[0] > 1:
                range_of_days.append([last_day, i - 1])
                range_of_days.append([i, i])
                last_day = i + 1
            elif dfCarOne['Дата трн.'][list_of_gas_station_days.index(i)].hour < 12:
                range_of_days.append([last_day, i - 1])
                last_day = i
                if i == days_in_month[1]:
                    range_of_days.append([i, i])
            else:
                range_of_days.append([last_day, i])
                last_day = i + 1
            if i == list_of_gas_station_days[-1] and i != days_in_month[1]:
                range_of_days.append([last_day, days_in_month[1]])

    # Range of gas consumption
    last_day = 1
    if list_of_gas_station_days.count(1) == 0:
        if dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])].shape[0] > 1:
            if gas_leftover_by_start_of_month <= 11:
                remains = gas_leftover_by_start_of_month
                gas_capacity = remains
                gas_capacity_list.append(remains)
                gas_leftover.append(gas_leftover_by_start_of_month - remains)
                gas_leftover.append(sum(dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])]['Кол-во'][:-1]) + gas_capacity)
                gas_capacity = dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])]['Кол-во'].iloc[-1]
                gas_capacity_list.append(gas_capacity)
            else:
                remains = (random() * ((tank_capacity - dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])]['Кол-во'].iloc[0] - gas_leftover_by_start_of_month) / 2)) + ((tank_capacity - dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])]['Кол-во'].iloc[0] - gas_leftover_by_start_of_month) / 2)
                gas_capacity_list.append(remains)
                gas_leftover.append(gas_leftover_by_start_of_month - remains)
                gas_leftover.append(sum(dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])]['Кол-во'][:-1]) + gas_capacity)
                gas_capacity = dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])]['Кол-во'].iloc[-1]
                gas_capacity_list.append(gas_capacity)
            last_day = list_of_gas_station_days[0] + 1

        elif dfCarOne['Дата трн.'][list_of_gas_station_days[0]].hour < 12:
            if gas_leftover_by_start_of_month <= 11:
                remains = gas_leftover_by_start_of_month
            else:
                remains = (random() * ((tank_capacity - dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])]['Кол-во'].iloc[0] - gas_leftover_by_start_of_month) / 2)) + ((tank_capacity - dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])]['Кол-во'].iloc[0] - gas_leftover_by_start_of_month) / 2)
            gas_capacity_list.append(remains)
            gas_leftover.append(gas_leftover_by_start_of_month - remains)
            gas_capacity = remains + sum(dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])]['Кол-во'])
            gas_capacity_list.append(gas_capacity)
            last_day = list_of_gas_station_days[0]
        else:
            if gas_leftover_by_start_of_month <= 11:
                remains = (random() * gas_leftover_by_start_of_month / 2)
            else:
                remains = (random() * gas_leftover_by_start_of_month / 2)
            gas_leftover.append(gas_leftover_by_start_of_month - remains)
            gas_capacity = remains + sum(dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[0])]['Кол-во'])
            gas_capacity_list.append(gas_capacity)
            last_day = list_of_gas_station_days[0] + 1

    for i in range(last_day, days_in_month[1] + 1):
        if list_of_gas_station_days.count(i) != 0:
            if dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)].shape[0] > 1:
                if i != list_of_gas_station_days[-1]:
                    remains = (random() * ((tank_capacity - dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[list_of_gas_station_days.index(i) + 1])]['Кол-во'].iloc[0]) / 2)) + (tank_capacity - dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[list_of_gas_station_days.index(i) + 1])]['Кол-во'].iloc[0]) / 2
                else:
                    remains = gas_leftover_by_end_of_month
                gas_leftover.append(gas_capacity - remains)
                gas_leftover.append(remains + sum(dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)]['Кол-во'][1:]))
                gas_capacity = dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)]['Кол-во'][0]
                gas_capacity_list.append(gas_capacity)
            elif dfCarOne['Дата трн.'][list_of_gas_station_days.index(i)].hour < 12:
                if i != list_of_gas_station_days[-1]:
                    remains = (random() * ((tank_capacity - dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[list_of_gas_station_days.index(i)])]['Кол-во'].iloc[0]) / 2)) + (tank_capacity - dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[list_of_gas_station_days.index(i)])]['Кол-во'].iloc[0]) / 2
                else:
                    remains = gas_leftover_by_end_of_month
                gas_leftover.append(gas_capacity - remains)
                gas_capacity = sum(dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)]['Кол-во']) + remains
                gas_capacity_list.append(gas_capacity)
            else:
                if i != list_of_gas_station_days[-1]:
                    remains = (random() * ((tank_capacity - dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[list_of_gas_station_days.index(i)])]['Кол-во'].iloc[0]) / 2)) + (tank_capacity - dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == list_of_gas_station_days[list_of_gas_station_days.index(i)])]['Кол-во'].iloc[0]) / 2
                else:
                    remains = gas_leftover_by_end_of_month
                gas_leftover.append(gas_capacity - remains)
                gas_capacity = sum(dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)]['Кол-во']) + remains
                gas_capacity_list.append(gas_capacity)
            if i == list_of_gas_station_days[-1] and i != days_in_month[1]:
                gas_leftover.append(gas_capacity - gas_leftover_by_end_of_month)
                gas_capacity = gas_leftover_by_end_of_month
                gas_capacity_list.append(gas_leftover_by_end_of_month)
            elif i == list_of_gas_station_days[-1]:
                gas_leftover.append(gas_capacity +  sum(dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)]['Кол-во']) - gas_leftover_by_end_of_month)
                gas_capacity = gas_leftover_by_end_of_month
                gas_capacity_list.append(gas_leftover_by_end_of_month)
    if gas_capacity_list[-1] > gas_leftover_by_end_of_month:
        gas_leftover[-1] = gas_leftover[-1] + gas_capacity_list[-1] - gas_leftover_by_end_of_month
        gas_capacity_list[-1] = gas_leftover_by_end_of_month
    for i in range(len(gas_leftover)):
        gas_leftover[i] = round(gas_leftover[i], 1)
    for i in range(len(gas_capacity_list)):
        gas_capacity_list[i] = round(gas_capacity_list[i], 1)
    mark_list = []
    for i in list_of_gas_station_days:
        mark_list.append(dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)]['Услуга'].reset_index(drop=True)[0])

    return [range_of_days, gas_leftover, gas_capacity_list, list_of_gas_station, list_of_gas_station_days, mark_list]










