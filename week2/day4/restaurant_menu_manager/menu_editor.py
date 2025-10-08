from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\nMENU MANAGER")
        print("(V) View an Item")
        print("(A) Add an Item")
        print("(D) Delete an Item")
        print("(U) Update an Item")
        print("(S) Show the Menu")
        print("(E) Exit")

        choice = input("Choose an option: ").upper()

        if choice == "V":
            name = input("Enter item name: ")
            item = MenuManager.get_by_name(name)
            print("Found:", item if item else "Not found.")

        elif choice == "A":
            name = input("Enter item name: ")
            price = int(input("Enter item price: "))
            MenuItem(name, price).save()

        elif choice == "D":
            name = input("Enter item name to delete: ")
            MenuItem(name, 0).delete()

        elif choice == "U":
            name = input("Enter item name to update: ")
            price = int(input("Enter current price: "))
            new_name = input("Enter new item name: ")
            new_price = int(input("Enter new item price: "))
            MenuItem(name, price).update(new_name, new_price)

        elif choice == "S":
            print("\nRestaurant Menu:")
            for i in MenuManager.all_items():
                print(f"{i[0]} - {i[1]} : {i[2]} MAD")

        elif choice == "E":
            print("\nExiting... Final Menu:")
            for i in MenuManager.all_items():
                print(f"{i[0]} - {i[1]} : {i[2]} MAD")
            break

        else:
            print("Invalid option, try again.")
