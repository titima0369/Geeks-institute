basket = ["Banana", "Apples", "Oranges", "Blueberries"]


basket.remove("Banana")
basket.remove("Blueberries")


basket.append("Kiwi")


basket.insert(0, "Apples")


apple_count = basket.count("Apples")
print("Number of apples:", apple_count)

basket.clear()


print("Final basket:", basket)