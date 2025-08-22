class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.imals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        groups = {}
        
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        
        return groups

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


new_york_zoo = Zoo("New York Zoo")


new_york_zoo.add_animal("Lion")
new_york_zoo.add_animal("Tiger")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Elephant")
new_york_zoo.add_animal("Monkey")


new_york_zoo.get_animals()


new_york_zoo.sell_animal("Bear")
new_york_zoo.get_animals()


new_york_zoo.get_groups()