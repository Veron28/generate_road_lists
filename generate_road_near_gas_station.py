from rast import addres_near


def generate_road_near_gas_station(df, days, car):
    df = df[df['Ед. изм.'] == 'л']
    if car == 1:
        dfCarOne = df[(df['Карта'] == 3005541161)]  # Машина 1
    else:
        dfCarOne = df[(df['Карта'] == 3005541160) | (df['Карта'] == 3005541162)]  # Машина 2
    dfCarOne = dfCarOne[['Дата трн.', 'Услуга', 'Кол-во', 'Адрес ТО']][::-1].reset_index(drop=True)
    mass = []
    for i in days:
        if (dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)])['Дата трн.'].reset_index(drop=True)[0].hour < 12:
            pos_gas = 'start'
        else:
            pos_gas = 'end'
        mass.append([i, addres_near((dfCarOne[dfCarOne['Дата трн.'].apply(lambda x: x.day == i)])['Адрес ТО'].reset_index(drop=True)[0]), pos_gas])

    return mass