"""
numbers = [86, 23, 65, 12, 54, -23, 23, 532, 65]
sum = 0

for n in numbers:
    if n > 20:
        sum += 1

print(sum)
"""
"""
numbers = [12, 23, 34, 45, 56, 67, 78, 89, 90]
summ = 0

for i in numbers:
    if i % 3 == 0:
        summ += i

print(summ)
"""

"""
numbers = [12, 23, 34, 45, 56, 67, 78, 89, 90]
print(sum(i for i in numbers if i % 3 == 0))

strings = ['asdasd', ' asdasd', 'sdasdas', 'd  sad asdsad']
print(sum(len(i) for i in strings if ' ' not in i))
"""
"""
names = []

count = 10
for i in range(count):
    name = input("Имя, кого вы хотите пригласить?\n")
    if name not in names:
        names.append(name)

print("Имена тех, кто пойдет на вечеринку:", *names)
"""
#Старт
bucket = []
print("""Вы пришли магазин, выберите действие:
    1. Добавить товар в корзину
    2. Убрать товар из корзины
    3. Посмотреть, что сейчас лежит в корзине
    4. Закончить выбор товаров""")
while True:
    string = input()
    if "добавить" in string.lower():
        bucket.append(string.lower().replace("добавить ", ""))
    elif "убрать" in string.lower():
        bucket.remove(string.lower().replace("убрать ", ""))
    elif "посмотреть" in string.lower():
        print(*bucket)
    elif "закончить" in string.lower():
        print(f"Вы выходите из магазина с такими покупками:")
        print(*bucket)
        break
    else:
        print("Вы ввели неправильную команду")