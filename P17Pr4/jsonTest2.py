import json


# функцию невозможно сериализовать, поэтому при попытке перенести
# этот файл в json появится ошибка
# рассмотрим решение этой проблемы в классе pickleTest.py
def player_attack():
    print("ATTACK!")


players = {
    "BigMover": {
        "Level": 2,
        "Health": 100,
        "Attack": player_attack
    }
}

json.dump(players, open("Players.json", "w", encoding="utf-8"),
          indent=4, ensure_ascii=False)
