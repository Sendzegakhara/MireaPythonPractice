# TODO: условия, циклы, списки и словари

"""
username = input("Username: ")
if username == "admin":
    print("Вы успешно авторизированы в системе")
else:
    print("Логин неверен")

print("Выход из программы")
"""
"""
number = int(input("Число: "))

if number > 0:
    print(f"Число {number} положительное")
else:
    print(f"Число {number} отрицательное")
"""
"""
tempa = int(input("Температура: "))

if tempa > 30:
    print("Ух какая жара")
elif tempa > 12:
    print("Какая хорошая погода")
elif tempa > 0:
    print("Неплохо, но ветерок")
elif tempa > -12:
    print("Холодновато, нужна куртка")
elif tempa > -30:
    print("Срочно нужен шарф и варежки")
else:
    print("Я из дома сегодня не ходок")
"""

"""
counter = 0;

for i in range(1000, 100, -1):
    if i % 10 == 0:
        print(i)
        counter += 1
print(counter)
"""
"""
login = input("Login: ")

while login == "":
    print("Invalid login: empty")
    login = input("Login: ")
"""
"""
login = input("Login: ")

while login != "admin":
    print("Invalid login")
    login = input("Login: ")
"""
"""
while True:
    cmd = input("CMD: ")

    if cmd == "exit":
        break
"""
"""
number = 10

while number > 1:
    print(number)
    number -= 1
else:
    print("END")
"""

"""
numbers = [8, 6, 3, "asdasd"]
print(numbers)
"""
"""
numbers = [8, 5, 9, -2, 4, 3]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)
"""
"""
numbers = [8, 5, 9, -2, 4, 3]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
"""
"""
contacts = []

while True:
    contact = input("Name: ")
    if contact in contacts:
        print('Данный контакт уже существует')
    elif contact == "remove":
        removed = input("Какой контакт Вы хотите удалить: ")
        contacts.remove(removed)
        print(f"Контакт {removed} удален")
    elif contact == "exit":
        break
    else:
        contacts.append(contact)
        print(f"Контакт {contact} добавлен в список")
"""
"""
names = ["Даня", "Ваня", "Игорь"]
print(*names)
"""

titles = ["Главная соц-сеть страны!", "Сайт мэра Москвы!",
          "Госуслуги", "Поисковая строка"]

for title in titles:
    index = titles.index(title)
    titles[index] = title.upper()
print(titles)

for i in range(len(titles)):
    titles[i] = titles[i].lower()
print(titles)

titles = list(map(lambda x: x.replace(" ", "_").upper(), titles))
print(titles)

numbers = [10, 12, 42, -2, 0, 7]
print(numbers)
print(list(map(lambda n: n**2, numbers)))
print(list(map(lambda n: n > 0, numbers)))