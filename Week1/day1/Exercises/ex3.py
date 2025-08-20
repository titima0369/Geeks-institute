user_name = input("Hello! I'm Fatima Ezzahra  What's your name? ").strip().title()

assistant_name = "Fatima Ezzahra"

if user_name.lower() == assistant_name.lower():
    print("\n WHOA! We're name twins! ")
   
else:
    print(f"\n Lovely to meet you, {user_name}! ")