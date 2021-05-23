#Importing the Nominatim geocoder class
from geopy.geocoders import Nominatim
import pandas as pd
from geopy.distance import geodesic

def addres_near(address):
    geolocator = Nominatim(user_agent="my_request")

    df = pd.read_excel('Адреса.xlsx', engine='openpyxl', index_col=0)
    coord_list = []
    for i in df.columns:
        if i == 'Большой проспект Васильевского острова, 42':
            coord_list.append([i, (59.935565, 30.272488)])
        elif i.count('Кронштадт') != 0 or i.count('Сестрорецк') != 0:
            location = geolocator.geocode(i)
            coord_list.append([i, (location.latitude, location.longitude)])
        else:
            location = geolocator.geocode(i + ' , г. Санкт-Петербург')
            coord_list.append([i, (location.latitude, location.longitude)])
    coord_list = coord_list[1:]
    df = pd.read_excel('TransactionsTableАпрель.xls', engine='xlrd', header=2)

    gas_coord = []

    for i in [address]:
        n = 4
        if i.split(',')[-2] != 'Россия':
            n = 3

        if (',').join(i.split(',')[:4]) == 'г. Санкт-Петербург, г. Сестрорецк, Приморское шоссе, 315':
            location ='г. Сестрорецк, Приморское шоссе, 315'
        elif i.split(',').count('Сестрорецк') != 0:
            location = (',').join(i.split(',')[:n])
        elif i.count('ш.') == 1:
            location = (',').join(i.split(',')[:n]).replace('ш.', 'шоссе')
        elif i.count('пр.') == 1:
            location = (',').join(i.split(',')[:n]).replace('пр.', 'проспект')
        elif i.count('пр-т.') == 1:
            location = (',').join(i.split(',')[:n]).replace('пр-т.', 'проспект')
        elif i.count('ул.') == 1:
            location = (',').join(i.split(',')[:n]).replace('ул.', 'улица')
        else:
            location = (',').join(i.split(',')[:n])
        try:
            if location.split(' ').index('улица') == 0:
                location = location.split(',')[0].split(' ')[1] + ' ' + location.split(',')[0].split(' ')[0] + ',' +  (',').join(location.split(',')[1:n])
        except:
            pass
        try:
            if location.split(',')[1].count('лит1') == 1:
                location = location.split(',')[0] +  ',' + location.split(',')[1].replace("лит1", "") + (',').join(
                        location.split(',')[2:n])
        except:
            pass
        try:

            location1 = geolocator.geocode(location)
            gas_coord.append([location1, (location1.latitude, location1.longitude)])
        except:
            if location.split(',')[0].split(' ').index('улица') == 1:
                location = location.split(',')[0].split(' ')[1] + ' ' + location.split(',')[0].split(' ')[0] + ',' + (
                    ',').join(location.split(',')[1:n])
            location1 = geolocator.geocode(location)
            if location1 == None:
                gas_coord.append([location1, (0, 0)])
            else:
                gas_coord.append([location1, (location1.latitude, location1.longitude)])


    for i in gas_coord:
        minn = 100000000
        ans = 0
        for j in coord_list:
            if geodesic(i[1], j[1]).km < minn:
                minn = geodesic(i[1], j[1]).km
                ans = j[0]
    return ans

