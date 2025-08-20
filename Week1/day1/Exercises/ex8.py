sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", 
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", 
                   "Pastrami sandwich"]


print("The deli has run out of Pastrami sandwiches!\n")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")


finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  
    print(f"I made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)


print("\n--- Finished sandwiches ---")
for sandwich in finished_sandwiches:
    print(f" {sandwich}")