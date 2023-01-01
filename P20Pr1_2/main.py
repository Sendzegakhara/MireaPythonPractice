# TODO: объекты и классы

class Bird:
    age = 2
    weight = 0.4
    color = "Gray"
    bird_type = "Sparrow"

    access_food = ["bread", "corn", "apple"]

    def __init__(self, age, weight, color, bird_type):
        self.age = age
        self.weight = weight
        self.color = color
        self.bird_type = bird_type

    def twitter(self):
        print(self.color + " " + self.bird_type + " " + "twitter")

    def eat(self, food):
        if food.name.lower() in self.access_food:
            print(self.color + " " + self.bird_type + " eat " + food.name
                  + f" {food.weight}")
            self.weight += food.weight
            print(f"Now bird's weight equals {self.weight}")
        else:
            print("Bird doesn't eat this")

    def fly(self):
        if self.weight > 0.5:
            print("Bird cannot fly because it's very fat")
        else:
            print(self.color + " " + self.bird_type + " flying")


class Food:
    weight = 0.5
    name = "Corn"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


food = Food("Bread", 0.04)
bird = Bird(3, 0.4, "Blue", "Sparrow")
bird.twitter()
bird.color = "Red"
bird.bird_type = "Raven"
bird.twitter()
bird.eat(food)
bird.fly()
food.name = "Pear"
bird.eat(food)
food.name = "Corn"
food.weight = 0.7
bird.eat(food)
bird.fly()
