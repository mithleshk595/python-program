
# try:
#     f = open("demo.txt", "r")
#     data = f.read()
#     f.close()
# except FileNotFoundError:
#     print("File 'demo.txt' not found.")


# f = open("demo.txt", "r")

# print(f.read())

# def add( x, y ):
#     return x + y
# def substract( x, y ):
#     return x - y
# def multiply( x, y ):
#     return x * y
# def divide( x, y):
#    if y!= 0:
#     return x / y
#    else:
#        "error! division by zero"

# print("select operation:")
# print("1 Add")
# print("2 Substract")
# print("3 Multiply")
# print("4 divide")

# choice =input("enter choice (1/2/3/4): ")

# num1 = float(input("enter first number :"))
# num2 = float(input("enter second number :"))

# if choice == '1':
#     print("result= ", add(num1, num2))
# elif choice == '2':
#     print("result=",substract(num1, num2))
# elif choice =='3':
#     print("result= ", multiply(num1, num2))
# elif choice == '4':
#     print("result= ", divide(num1, num2))
# else:
#     print("invalid number")


import calendar   # calendar module import karna h

# input year and month
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# print the calendar for given month
print("\n", calendar.month(year, month))

import calendar # calendar module import karna h

# input year and month
year = int(input("enter year:"))
month = int(input("enter month (1-12): "))

#print the calendar for given month
print("\n", calendar.month(year, month))