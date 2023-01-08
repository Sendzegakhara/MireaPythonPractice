numbers_counter = {}
directory = "../Task3/"

for i in range(25):
    name = f"file{i}.txt"

    with open(directory + name, "r", encoding="utf-8") as file:
        data = file.read()
        numbers = list(data)

        for number in numbers:
            if number in numbers_counter.keys():
                numbers_counter[number] += 1
            else:
                numbers_counter[number] = 1

print(numbers_counter)