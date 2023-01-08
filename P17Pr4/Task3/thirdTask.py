# TODO: 3) Создать 25 файлов и
#  заполнить их 10 случайными числами

from random import randrange

for name in range(25):
    string = f"file{name}.txt"
    file = open(string, "w")
    for number in range(10):
        file.write(str(randrange(10)))
