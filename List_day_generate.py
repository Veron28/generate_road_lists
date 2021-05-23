import pandas as pd
import calendar
import datetime


try:
    df = pd.read_excel('TransactionsTableАпрель.xls', engine = 'openpyxl', header = 2)
except Exception:
    df = pd.read_excel('TransactionsTableАпрель.xls', engine='xlrd', header=2)
car = 1

df = df[df['Ед. изм.'] == 'л']
if car == 1:
    dfCarOne = df[(df['Карта'] == 3005541161)]  # Машина 1
else:
    dfCarOne = df[(df['Карта'] == 3005541160) | (df['Карта'] == 3005541162)]  # Машина 2
dfCarOne = dfCarOne[['Дата трн.', 'Услуга', 'Кол-во']][::-1].reset_index(drop=True)
month_num = dfCarOne['Дата трн.'][0].month
days_in_month = calendar.monthrange(dfCarOne['Дата трн.'][0].year, dfCarOne['Дата трн.'][0].month)

list_day = []
for i in range(1,  days_in_month[1] + 1):
    list_day.append(str(datetime.date(datetime.date.today().year, month_num, i)).replace('-', '.'))

print(list_day)