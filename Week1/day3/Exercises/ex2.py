class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")


davids_dog = Dog("Rex", 50)
print(f"David's dog: Name: {davids_dog.name}, Height: {davids_dog.height}cm")
davids_dog.bark()
davids_dog.jump()


sarahs_dog = Dog("Teacup", 20)
print(f"\nSarah's dog: Name: {sarahs_dog.name}, Height: {sarahs_dog.height}cm")
sarahs_dog.bark()
sarahs_dog.jump()


if davids_dog.height > sarahs_dog.height:
    print(f"\nThe bigger dog is {davids_dog.name}")
else:
    print(sarahs_dog.name, "is bigger.")