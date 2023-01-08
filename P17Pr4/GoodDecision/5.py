directory = "../Task3/"
summator = 0

for i in range(25):
    name = f"file{i}.txt"

    with open(directory + name, "r", encoding="utf-8") as file:
        data = file.read()
        summator += sum(list(map(int, data)))

print(summator)