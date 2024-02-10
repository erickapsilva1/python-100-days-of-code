import datetime as dt

now = dt.datetime.now()

print(now.year)
print(now.month)
print(now.hour)
print(now.weekday())

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)