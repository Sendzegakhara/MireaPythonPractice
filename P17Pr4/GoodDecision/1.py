# благодаря конструкции with open, можно не
# закрывать файла после работы с ним

with open("3.txt", "w", encoding="utf-8") as output:
    for filename in ["1.txt", "2.txt"]:
        with open(filename, "r", encoding="utf-8") as file:
            output.write(file.read() + "\n")