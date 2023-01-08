# TODO : 4) Найти сколько чисел повторилось
# в 25 файлах из 3-ей задачи

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
zero = 0

for name in range(25):
    string = f"../Task3/file{name}.txt"
    file = open(string, 'r')
    data = file.read()
    for number in data:
        match int(number):
            case 1:
                one += 1
            case 2:
                two += 1
            case 3:
                three += 1
            case 4:
                four += 1
            case 5:
                five += 1
            case 6:
                six += 1
            case 7:
                seven += 1
            case 8:
                eight += 1
            case 9:
                nine += 1
            case 0:
                zero += 1

print(f"one: {one}\ntwo: {two}\nthree: {three}\nfour: {four}\nfive {five}"
      f"\nsix: {six}\nseven: {seven}\neight: {eight}\nnine: {nine}\nzero: {zero}")
