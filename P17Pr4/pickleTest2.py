import pickle

'''
def player_attack():
    print("ATTACK!")

players = {
    "Player1": {
        "Health": 100,
        "Level": 2,
        "Attack": player_attack
    }
}

pickle.dump(players, open("Players.pkl", "wb"))

data = dict(pickle.load(open("Players.pkl", "rb")))
data["Player1"]["Attack"]()
'''


class Player:
    name = ""
    health = 100
    armor = 10
    hand_item = "Axe"

    def __init__(self, name, health, hand_item):
        self.name = name
        self.health = health
        self.hand_item = hand_item

    def say_hello(self):
        print(f"Player {self.name} say Hello to you!")

player = Player("Vasya", 100, "minigun")
pickle.dump(player, open("Player.pkl", "wb"))
data = pickle.load(open("Player.pkl", "rb"))
data.say_hello()
print(type(data))
# Таким образом, pickle позволяет сохранять состояния
# функций, классов, объектов и т.д.