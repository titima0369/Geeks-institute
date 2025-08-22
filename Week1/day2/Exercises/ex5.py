import random

def compare_numbers(user_number):
   
    random_number = random.randint(1, 100)
    
    
    if user_number == random_number:
        print("Success! The numbers match!")
    else:
        print("Fail! The numbers are different.")
        print(f"Your number: {user_number}")
        print(f"Random number: {random_number}")

