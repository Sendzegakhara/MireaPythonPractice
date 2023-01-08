import datetime

start = datetime.datetime.now()

summator = 0

for i in range(10000):
    if i % 3 == 0 and i % 5 != 0:
        summator += i

end = datetime.datetime.now()

print(summator)
print(end - start)

# Но datetime лучше не использовать для таких целей.
# Для этого есть специальные тесты, юнит-тесты...

# https://pythononline.ru/osnovy/strptime-python

time = datetime.datetime.now()
print(time.strftime("Сегодня %A %d.%m.%Y, а время %H:%M.%S"))

time_str = "10.10.2022 18:45.07"
time = datetime.datetime.strptime(time_str, "%d.%m.%Y %H:%M.%S")
print(time)