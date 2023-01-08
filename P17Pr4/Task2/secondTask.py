# TODO: 2) Есть два файла, нужно поменять
#  данные файлов местами

file1 = open("../Task1/for11.txt", "r")
file2 = open("../Task1/for12.txt", "r")

data1 = file1.readlines()
data2 = file2.readlines()

file1.close()
file2.close()

file1 = open("../Task1/for11.txt", "w")
file2 = open("../Task1/for12.txt", "w")

for f in data1:
    file2.write(f)

for f in data2:
    file1.write(f)