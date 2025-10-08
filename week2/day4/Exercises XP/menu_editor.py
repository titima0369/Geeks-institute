
from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\n====== Program Menu ======")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("X - Exit")
        choice = input("Please choose an option: ").upper()

        if choice == "V":
            view_item()
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "X":
            print("\nExiting program... Here is the final menu:\n")
            show_restaurant_menu()
            break
        else:
            print("Invalid choice, try again.")


def add_item_to_menu():
    name = input("Enter the item name: ")
    price = input("Enter the item price: ")

    try:
        item = MenuItem(name, float(price))
        item.save()
        print(f"{name} was added successfully.")
    except Exception as e:
        print(f"Error adding item: {e}")

def view_item():
    name = input("Enter the item name to view: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Item: {item.name}, Price: {item.price}")
    else:
        print("Item not found.")

def remove_item_from_menu():
    name = input("Enter the item name to remove: ")
    item = MenuItem(name, 0)
    if item.delete():
        print(f"{name} was removed successfully.")
    else:
        print("Item not found or could not be removed.")

def update_item_from_menu():
    name = input("Enter the item name to update: ")
    price = input("Enter the new price: ")
    item = MenuItem(name, float(price))
    if item.update():
        print(f"{name} was updated successfully.")
    else:
        print("Item not found or could not be updated.")

def show_restaurant_menu():
    menu = MenuManager.all()
    print("\n--- Restaurant Menu ---")
    for item in menu:
        print(f"{item.name}: ${item.price}")
    if not menu:
        print("Menu is empty.")