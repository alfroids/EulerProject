import datetime as dt

start_date = dt.date(1901, 1, 1)
end_date = dt.date(2000, 12, 31)

date = start_date
count = 0

while date <= end_date:
    count += date.weekday() == 6 and date.day == 1
    date += dt.date.resolution

print(count)
