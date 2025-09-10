# Part I - Review about arrays
people = ["Greg", "Mary", "Devon", "James"]


people.pop(0)


people[people.index("James")] = "Jason"


people.append("YourName")


print("Mary index:", people.index("Mary"))


new_people = people[1:len(people)-1]
print("Copy without Mary and YourName:", new_people)


print("Index of Foo:", people.index("Foo") if "Foo" in people else -1)


last = people[-1]
print("Last person:", last)

# Part II - Loops
print("All people:")
for person in people:
    print(person)

print("Stop after Devon:")
for person in people:
    print(person)
    if person == "Devon":
        break
