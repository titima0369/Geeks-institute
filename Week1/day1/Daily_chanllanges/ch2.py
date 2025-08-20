user_input = input("Enter a string: ")


result = ""


for i in range(len(user_input)):
   
    if i == 0 or user_input[i] != user_input[i-1]:
        result += user_input[i]


print("String with duplicates removed:", result)