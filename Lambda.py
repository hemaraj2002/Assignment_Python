
max_of_three = lambda a, b, c: a if a > b and a > c else (b if b > c else c)


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))


print("The largest number is:", max_of_three(a, b, c))
