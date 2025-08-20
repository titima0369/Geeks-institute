my_fav_numbers = {7, 14, 21, 28}
print("My favorite numbers:", my_fav_numbers)


my_fav_numbers.add(35)
my_fav_numbers.add(42)
print("After adding two numbers:", my_fav_numbers)


my_fav_numbers.remove(28)  
print("After removing the last number:", my_fav_numbers)


friend_fav_numbers = {3, 6, 9, 12}
print("Friend's favorite numbers:", friend_fav_numbers)


our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our combined favorite numbers:", our_fav_numbers)