number = int(input("Enter a number: "))
length = int(input("Enter the length: "))


multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)


print("The list of multiples is:", multiples)