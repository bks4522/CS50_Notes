class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)


class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.is_Sitting = isSitting

    def sit_down(self):
        self.is_Sitting = True

    def stand_up(self):
        self.is_Sitting = False


p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
