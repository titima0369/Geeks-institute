# part2

def get_ticket_price(age):
    if age < 3:
        return 0
    elif age <= 12:
        return 10
    else:
        return 15

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

total_cost = 0
print("Ticket prices:")

for name, age in family.items():
    price = get_ticket_price(age)
    print(f"- {name.capitalize()} (age {age}): ${price}")
    total_cost += price

print(f"\nTotal cost for the family: ${total_cost}")

# part2
family = {}
total_cost = 0
num_members = int(input("Enter number of family members: "))

for i in range(num_members):
    name = input(f"Enter name of member {i+1}: ")
    age = int(input(f"Enter age for {name}: "))
    family[name] = age

print("\nTicket Prices:")
for name, age in family.items():
    price = get_ticket_price(age)
    total_cost += price
    print(f"{name}: ${price}")

print(f"\nTotal Cost: ${total_cost}")