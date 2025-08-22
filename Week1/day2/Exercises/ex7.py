import random

def get_random_temp(season):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "spring":
        return random.randint(10, 22)
    elif season == "summer":
        return random.randint(20, 40)
    elif season == "autumn":
        return random.randint(5, 20)
    else:
        return random.randint(-10, 40)

def main():
    season = input("Enter a season (winter, spring, summer, autumn): ").lower()
    temp = get_random_temp(season)
    
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif temp <= 23:
        print("Cool but nice weather.")
    elif temp <= 32:
        print("Warm weather, perfect for outside!")
    else:
        print("It's really hot! Stay hydrated.")


main()