import datetime

import pandas as pd

current_time = datetime.datetime.now()

print(current_time)

current_hour, current_minute = datetime.datetime.time(current_time).hour, datetime.datetime.time(current_time).minute

print('Hora atual: ', current_hour)
print('Minuto atual: ', current_minute)

current_date = datetime.datetime.date(datetime.datetime.today())

print('Data atual: ', current_date)