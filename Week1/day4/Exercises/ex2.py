class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} won the fight!"
        else:
            return f"{other_dog.name} won the fight!"


dog1 = Dog("laarbi", 5, 20)
dog2 = Dog("bojama", 3, 15)
dog3 = Dog("thami", 6, 25)

print(dog1.bark())
print(dog1.run_speed())
print(dog1.fight(dog2))
print(dog2.fight(dog3))
