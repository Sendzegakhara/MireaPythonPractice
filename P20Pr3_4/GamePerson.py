# TODO: поставить ограничения на перменные

class Person:
    name = "my name"
    age = 20
    hunger = 0
    thirst = 0
    fatigue = 0
    eat_count = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dig(self):
        if self.live_check() == True:
            print("You're digging\n")
            self.work()
        else:
            print("You're tired. You cannot do it...\n")

    def hunt(self):
        if self.live_check() == True:
            print("You're hunting\n")
            self.work()
            self.eat_count += 3
        else:
            print("You're tired. You cannot do it...\n")

    def eat(self):
        self.hunger -= 20
        self.eat_count -= 1
        print("You're eating\n")

    def drink(self):
        self.thirst -= 20
        print("You're drinking\n")

    def sleep(self):
        self.fatigue -= 50
        print("You're sleeping\n")

    def status_check(self):
        print(f"""Your stats:
        Eat count - {self.eat_count}
        Hunger - {self.hunger}
        Thirst - {self.thirst}
        Fatigue - {self.fatigue}\n""")

    def work(self):
        self.hunger += 18
        self.thirst += 14
        self.fatigue += 7

    def live_check(self):
        if self.fatigue >= 80 or self.thirst >= 80 or self.hunger >= 80:
            return False
        else:
            return True

print("Hello! Write your name and age to continue")
name = input("Name: ")
age = input("Age: ")
person = Person(name, age)
print("")

while True:
    action = input("""What you're gonna do?
    1. Dig
    2. Hunt
    3. Eat
    4. Drink
    5. Sleep
    6. Check your status
    7. Leave the game\n""")

    match action:
        case "1":
            person.dig()
        case "2":
            person.hunt()
        case "3":
            person.eat()
        case "4":
            person.drink()
        case "5":
            person.sleep()
        case "6":
            person.status_check()
        case "7":
            break
