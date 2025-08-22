class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members
    
    def born(self, **kwargs):
 
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} was born into the {self.last_name} family!")
    
    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False
    
    def family_presentation(self):
        print(f"Family {self.last_name}:")
        for member in self.members:
            print(f"  Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")


members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

smith_family = Family("Smith", members)


smith_family.born(name='John', age=0, gender='Male', is_child=True)
print(f"Is Michael over 18? {smith_family.is_18('Michael')}")
print(f"Is John over 18? {smith_family.is_18('John')}")
smith_family.family_presentation()