'''
Режим работы с файлами

    'r' - для чтения (по умолчанию)
    't' - текстовый режим (по умолчанию)
    'w' - для записи (перед открытием стирает все данные в файле)
    'a' - для записи (добавляет данные в конец файла)
    'x' - создает файл для записи
    'b' - двоичный режим
    '+' - расширение обычного флага
'''
# TODO : стандартное считывание и пасринг данных

users = {}

file = open("Config.txt", "r", encoding='utf-8')
lines = file.readlines()
file.close()

last_user = ""
last_user_login = ""
last_user_password = ""

for line in lines:
    if 'User-' in line:
        last_user = line.replace(':\n', '').replace(' ', '')
        continue
    if 'Login:' in line:
        last_user_login = line.replace('Login:', '').replace(' ', '').replace('\n', '')
        continue
    if 'Password:' in line:
        last_user_password = line.replace('Password:', '').replace(' ', '').replace('\n', '')
        users[last_user] = {'Login': last_user_login, 'Password': last_user_password}

print(users)