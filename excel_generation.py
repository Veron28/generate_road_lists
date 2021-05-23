import pandas as pd
from transaction1 import transaction
from generateRoads import generate_roads
from random import random
import datetime as dt
from generate_road_near_gas_station import generate_road_near_gas_station
import openpyxl as xl
import os




def excel_generation(gas_consumption, gas_leftover_by_start_of_month, gas_leftover_by_end_of_month, tank_capacity, excel_name_file, car_number, odometer_reading):
    if not os.path.exists("excel_forms"):
        os.mkdir("excel_forms")




    try:
        df = pd.read_excel(excel_name_file, engine = 'openpyxl', header = 2)
    except Exception:
        df = pd.read_excel(excel_name_file, engine='xlrd', header=2)

    year_now, month_now = df['Дата трн.'][0].year, df['Дата трн.'][0].month

    trans_list = transaction(df, gas_consumption, gas_leftover_by_start_of_month, gas_leftover_by_end_of_month, tank_capacity, car_number)

    gas = gas_leftover_by_start_of_month
    list_of_gas_station, list_of_gas_station_days = trans_list[3], trans_list[4]
    mark_list = trans_list[5]

    need_be = generate_road_near_gas_station(df, trans_list[4], car_number)

    need_be_loc = need_be



    for i in range(len(trans_list[0])):
        days = trans_list[0][i]
        gas_leftover = trans_list[1][i]
        gas_capacity = trans_list[2][i]

        week_days_loc = []
        for i in range(days[0], days[1] + 1):
            if dt.datetime(year_now, month_now, i).isoweekday() == 6 or dt.datetime(year_now, month_now, i).isoweekday() == 7:
                week_days_loc.append(i)
            elif (month_now == 12 and i == 31) or (month_now == 1 and i == 1) or (month_now == 1 and i == 2) or (month_now == 1 and i == 2) or (month_now == 2 and i == 23) or (month_now == 3 and i == 8) or (month_now == 5 and i == 1) or (month_now == 1 and i == 2):
                week_days_loc.append(i)
        week_days = []
        for i in week_days_loc:
            if list_of_gas_station_days.count(i) == 0:
                week_days.append(i)


        if list(set(range(days[0], days[1] + 1)) & set(trans_list[4])) == []:
            [roads, reminder, kilo] = generate_roads(len(range(days[0], days[1] + 1)) - len(week_days), gas_leftover, len(week_days),  gas_consumption, [])
        else:
            need_be_loc = [need_be[trans_list[4].index(i)] for i in list(set(range(days[0], days[1] + 1)) & set(trans_list[4]))]
            for j in range(len(need_be_loc)):
                need_be_loc[j][0] = need_be_loc[j][0] - days[0]
            [roads, reminder, kilo] = generate_roads(len(range(days[0], days[1] + 1)) - len(week_days), gas_leftover, len(week_days), gas_consumption, need_be_loc)
        if week_days != []:
            dayss = ([i for i in range(days[0], days[1] + 1) if i not in week_days])
            for i in week_days:
                dayss.append(i)
        else:
            dayss = [i for i in range(days[0], days[1] + 1) if i not in week_days]

        if len(dayss) != len(roads):
            for i in range(len(dayss) - len(roads)):
                roads.append([['Люботинский, 2-4', 'Люботинский, 2-4']])
                reminder.append(0)
                kilo.append(0)

        roads = [[dayss[i], roads[i]] for i in range(len(dayss))]
        reminder = [[dayss[i], reminder[i]] for i in range(len(dayss))]
        kilo = [[dayss[i], kilo[i]] for i in range(len(dayss))]
        roads = sorted(roads)
        reminder = sorted(reminder)
        kilo = sorted(kilo)
        roads = [i[1] for i in roads]
        reminder = [i[1] for i in reminder]
        kilo = [i[1] for i in kilo]

        if sum(reminder) == 0:
            attitude = 0
        else:
            attitude = gas_leftover / sum(reminder)
        for day in range(days[0], days[1] + 1):
            wb = xl.load_workbook(filename=f'form_{car_number}.xlsx')
            sheet = wb.active
            sheet['E2'] = dt.datetime(year_now, month_now, day)
            sheet['C10'] = dt.datetime(year_now, month_now, day)
            sheet['C11'] = dt.datetime(year_now, month_now, day)
            sheet['D10'] = '8:00'
            sheet['D11'] = '17:00'
            sheet['E10'] = odometer_reading
            sheet['C16'] = gas
            loc_rast = round(kilo[day - days[0]] + (random() * 5), 1)
            sheet['E12'] = loc_rast
            odometer_reading += loc_rast
            if list_of_gas_station_days.count(day) != 0:
                sheet['B16'] = mark_list[list_of_gas_station_days.index(day)]
                refueling = round(list_of_gas_station[list_of_gas_station_days.index(day)], 1)
                sheet['D16'] = refueling
                gas += refueling
            gas -= round((attitude * reminder[day - days[0]]), 1)
            gas = round(gas, 1)
            for pos, road in enumerate(roads[day - days[0]]):
                sheet[f'B{22 + pos}'] = road[0]
                sheet[f'C{22 + pos}'] = road[1]
            sheet['E11'] = odometer_reading
            sheet['E16'] = gas
            if len(roads[day - days[0]]) > 1:
                wb.save(
                    filename=f'excel_forms/{str(dt.datetime(year_now, month_now, day).year) + "_" + str(dt.datetime(year_now, month_now, day).month) + "_" + str(dt.datetime(year_now, month_now, day).day)}_{car_number}.xlsx')

        gas = gas_capacity
    return 'OK'
