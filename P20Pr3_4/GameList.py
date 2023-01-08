games_name = []
hours_in_game = []

while True:
    name = input("Write the name of the game: ")
    if name == "exit":
        print("Your stats:")
        for i in range(len(games_name)):
            print(games_name[i] + " - " + str(hours_in_game[i]))
        print("\nSummary hours in all games:")
        print(sum(hours_in_game))
        break
    elif name in games_name:
        print("That's game already in your list")
    else:
        games_name.append(name)
        hours = int(input("Write your hours in this game: "))
        hours_in_game.append(hours)
