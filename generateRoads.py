import pandas as pd
from numpy.random import choice
from graph import graph
from probability_distribution import probability_distribution
from from_number_to_address import from_number_to_address
from random import random






def generate_roads(days, liters_spent, weekdays, vehicle_consumption, need_be, build_graph = False):
    df = pd.read_excel('адреса.xlsx', engine='openpyxl', index_col=0)
    df_short_name = pd.read_excel('адреса.xlsx', engine='openpyxl', index_col=0)
    mass = []
    if need_be == []:
        for i in range(len(df.columns)):
            mass.append([i, df.columns[i], df_short_name.columns[i]])

        if weekdays == 0 or (weekdays != 0 and liters_spent <= (1.5 * vehicle_consumption) * days):
            n = 0
            start = []
            nodes_of_way = []
            list_of_addresses_used = []
            list_address = []

            for i in range(days):
                start.append([0, 0])
                nodes_of_way.append([['Люботинский, 2-4', 'Люботинский, 2-4']])
                list_of_addresses_used.append([])
                list_address.append(list(range(1, 14)))


            while sum((sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) / 100) * (vehicle_consumption * 1.1) for j in range(days)) <= liters_spent - (random() * 5):
                if len(list_of_addresses_used[n]) >= 3:
                    list_address[n].extend(list_of_addresses_used[n])
                    list_of_addresses_used[n] = []
                address = choice(list_address[n], 1, p=probability_distribution(list_address[n]))[0]
                list_address[n].remove(address)
                list_of_addresses_used[n].append(address)
                start[n].insert(-1, address)
                nodes_of_way[n] = from_number_to_address(start[n], mass)
                n += 1
                n = n % days


            if build_graph:
                for i in range(days):
                    graph(nodes_of_way[i], mass)


            return nodes_of_way, [(sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) / 100) * (vehicle_consumption * 1.1) for j in range(days)], [sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) for j in range(days)]


        else:
            n = 0

            start = []
            nodes_of_way = []
            list_of_addresses_used = []
            list_address = []

            for i in range(days):
                start.append([0, 0])
                nodes_of_way.append([['Люботинский, 2-4', 'Люботинский, 2-4']])
                list_of_addresses_used.append([])
                list_address.append(list(range(1, 14)))

            while sum(
                    (sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) / 100) * (vehicle_consumption * 1.1) for j in
                    range(days)) <= (4 * vehicle_consumption) * days:
                if len(list_of_addresses_used[n]) >= 3:
                    list_address[n].extend(list_of_addresses_used[n])
                    list_of_addresses_used[n] = []
                address = choice(list_address[n], 1, p=probability_distribution(list_address[n]))[0]
                list_address[n].remove(address)
                list_of_addresses_used[n].append(address)
                start[n].insert(-1, address)
                nodes_of_way[n] = from_number_to_address(start[n], mass)
                n += 1
                n = n % days
            n = 0

            start_for_week = []
            nodes_of_way_for_week = []
            list_of_addresses_used_for_week = []
            list_address_for_week = []

            for i in range(weekdays):
                start_for_week.append([0, 0])
                nodes_of_way_for_week.append([['Люботинский, 2-4', 'Люботинский, 2-4']])
                list_of_addresses_used_for_week.append([])
                list_address_for_week.append(list(range(1, 14)))

            while sum(
                    (sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way_for_week[j]) / 100) * (vehicle_consumption * 1.1) for j in
                    range(weekdays)) <= liters_spent - sum((sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) / 100) * (vehicle_consumption * 1.1) for j in range(days)):
                if len(list_of_addresses_used_for_week[n]) >= 3:
                    list_address_for_week[n].extend(list_of_addresses_used_for_week[n])
                    list_of_addresses_used_for_week[n] = []
                address = choice(list_address_for_week[n], 1, p=probability_distribution(list_address_for_week[n]))[0]
                list_address_for_week[n].remove(address)
                list_of_addresses_used_for_week[n].append(address)
                start_for_week[n].insert(-1, address)
                nodes_of_way_for_week[n] = from_number_to_address(start_for_week[n], mass)
                if ((sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way_for_week[n]) / 100) * (vehicle_consumption * 1.1)) > (4 * vehicle_consumption):
                    n += 1
                    n = n % weekdays

            nodes_of_way.extend(nodes_of_way_for_week)


            if build_graph:
                for i in range(len(nodes_of_way)):
                    graph(nodes_of_way[i], mass)
            return nodes_of_way, [(sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) / 100) * (vehicle_consumption * 1.1) for j in range(days + weekdays)], [sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) for j in range(days + weekdays)]
    else:
        for i in range(len(df.columns)):
            mass.append([i, df.columns[i], df_short_name.columns[i]])

        if weekdays == 0 or (weekdays != 0 and liters_spent <= (1.5 * vehicle_consumption) * days):
            n = 0
            start = []
            nodes_of_way = []
            list_of_addresses_used = []
            list_address = []
            day_need_be = [i[0] for i in need_be]
            pos_need_be = [list(df_short_name.columns).index(i[1]) for i in need_be]
            j = []

            for i in range(days):
                if day_need_be.count(i) == 0:
                    start.append([0, 0])
                    nodes_of_way.append([['Люботинский, 2-4', 'Люботинский, 2-4']])
                    list_of_addresses_used.append([])
                    list_address.append(list(range(1, 14)))
                    j.append(-1)
                else:
                    start.append([0, pos_need_be[day_need_be.index(i)], 0])
                    nodes_of_way.append([['Люботинский, 2-4', need_be[day_need_be.index(i)][1]], [need_be[day_need_be.index(i)][1], 'Люботинский, 2-4']])
                    list_of_addresses_used.append([pos_need_be[day_need_be.index(i)]])
                    list_address.append(list(range(1, 14)))
                    if need_be[day_need_be.index(i)][2] == 'start':
                        j.append(-1)
                    else:
                        j.append(-2)

            while sum(
                    (sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) / 100) * (vehicle_consumption * 1.1) for
                    j in range(days)) <= liters_spent - (random() * 5):
                if len(list_of_addresses_used[n]) >= 3:
                    list_address[n].extend(list_of_addresses_used[n])
                    list_of_addresses_used[n] = []
                address = choice(list_address[n], 1, p=probability_distribution(list_address[n]))[0]
                list_address[n].remove(address)
                list_of_addresses_used[n].append(address)
                start[n].insert(j[n], address)
                nodes_of_way[n] = from_number_to_address(start[n], mass)
                n += 1
                n = n % days

            if build_graph:
                for i in range(days):
                    graph(nodes_of_way[i], mass)
            return nodes_of_way, [
                (sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) / 100) * (vehicle_consumption * 1.1) for j in
                range(days)], [sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) for j in range(days)]


        else:
            n = 0

            start = []
            nodes_of_way = []
            list_of_addresses_used = []
            list_address = []
            day_need_be = [i[0] for i in need_be]
            pos_need_be = [list(df_short_name.columns).index(i[1]) for i in need_be]
            j = []

            for i in range(days):
                if day_need_be.count(i) == 0:
                    start.append([0, 0])
                    nodes_of_way.append([['Люботинский, 2-4', 'Люботинский, 2-4']])
                    list_of_addresses_used.append([])
                    list_address.append(list(range(1, 14)))
                    j.append(-1)
                else:
                    start.append([0, pos_need_be[day_need_be.index(i)], 0])
                    nodes_of_way.append([['Люботинский, 2-4', need_be[day_need_be.index(i)][1]], [need_be[day_need_be.index(i)][1], 'Люботинский, 2-4']])
                    list_of_addresses_used.append([pos_need_be[day_need_be.index(i)]])
                    list_address.append(list(range(1, 14)))
                    if need_be[day_need_be.index(i)][2] == 'start':
                        j.append(-1)
                    else:
                        j.append(-2)
            while sum(
                    (sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) / 100) * (vehicle_consumption * 1.1) for
                    j in
                    range(days)) <= (4 * vehicle_consumption) * days:
                if len(list_of_addresses_used[n]) >= 3:
                    list_address[n].extend(list_of_addresses_used[n])
                    list_of_addresses_used[n] = []
                address = choice(list_address[n], 1, p=probability_distribution(list_address[n]))[0]
                list_address[n].remove(address)
                list_of_addresses_used[n].append(address)
                start[n].insert(j[n], address)
                nodes_of_way[n] = from_number_to_address(start[n], mass)
                n += 1
                n = n % days
            n = 0

            start_for_week = []
            nodes_of_way_for_week = []
            list_of_addresses_used_for_week = []
            list_address_for_week = []

            for i in range(weekdays):
                start_for_week.append([0, 0])
                nodes_of_way_for_week.append([['Люботинский, 2-4', 'Люботинский, 2-4']])
                list_of_addresses_used_for_week.append([])
                list_address_for_week.append(list(range(1, 14)))

            while sum(
                    (sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way_for_week[j]) / 100) * (
                            vehicle_consumption * 1.1) for j in
                    range(weekdays)) <= liters_spent - sum(
                (sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) / 100) * (vehicle_consumption * 1.1) for j in
                range(days)):
                if len(list_of_addresses_used_for_week[n]) >= 3:
                    list_address_for_week[n].extend(list_of_addresses_used_for_week[n])
                    list_of_addresses_used_for_week[n] = []
                address = choice(list_address_for_week[n], 1, p=probability_distribution(list_address_for_week[n]))[0]
                list_address_for_week[n].remove(address)
                list_of_addresses_used_for_week[n].append(address)
                start_for_week[n].insert(-1, address)
                nodes_of_way_for_week[n] = from_number_to_address(start_for_week[n], mass)
                if ((sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way_for_week[n]) / 100) * (
                        vehicle_consumption * 1.1)) > (4 * vehicle_consumption):
                    n += 1
                    n = n % weekdays

            nodes_of_way.extend(nodes_of_way_for_week)

            if build_graph:
                for i in range(len(nodes_of_way)):
                    graph(nodes_of_way[i], mass)
            return nodes_of_way, [
                (sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) / 100) * (vehicle_consumption * 1.1) for j in
                range(days + weekdays)], [sum((df_short_name[i[0]])[i[1]] for i in nodes_of_way[j]) for j in range(days + weekdays)]
