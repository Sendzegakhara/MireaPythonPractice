# TODO : 1) Есть три файла, нужно всю
#  информацию из первых двух вставить в третий

def writeFunc(fileName, string):
    file = open(fileName, "w")
    file.write(string)
    file.close()


string1 = "123456\n7890-=\nqwerty\nuiop[]"
string2 = "asdfgh\njkl;'\nzxcvbn\nm,./c.xxc"

# writeFunc("for11.txt", string1)
# writeFunc("for12.txt", string2)

file1 = open("for11.txt")
file2 = open("for12.txt")

file1to3 = file1.readlines()
file2to3 = file2.readlines()

file3 = open("for13.txt", "a")

for f in file1to3:
    file3.write(f)
file3.write("\n")
for f in file2to3:
    file3.write(f)

file1.close()
file2.close()
file3.close()

data = open("for13.txt", "r")

print(data.read())
