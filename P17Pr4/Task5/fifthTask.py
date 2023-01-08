# TODO: 5) Сложить все числа из всех файлов

sum = 0

for name in range(25):
    string = f"../Task3/file{name}.txt"
    file = open(string, 'r')
    data = file.read()
    for i in data:
        sum += int(i)

print(sum)
sum = 0

for name in range(25):
    string = f"../Task3/file{name}.txt"
    file = open(string, 'r')
    data = file.read()
    sum += int(data)

print(sum)