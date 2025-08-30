def add( x, y):
    return x + y
def substract( x, y):
    return x - y
def multiply( x, y):
    return x * y
def divide( x, y):
    if y !=0:
        return x / y
    else:
        return "error! divison by zero"
print("select operation:")
print("1 Add")
print("2 Substract")
print("3 Multiply")
print("4 Divide")

choice = input("enter choice (1/2/3/4): ")

num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))


if choice == '1': 
    print("result =", add(num1, num2))
elif choice == '2':
    print("result =", substract(num1, num2))
elif choice == '3':
    print("result =", multiply(num1, num2))
elif choice == '4':
    print("result=", divide(num1, num2))
else:
    print("invalid user")
def add( x, y):
    return x + y
def substract( x, y):
    return x - y
def multiply( x , y):
    return x * y
def divide( x , y):
    if y!=0:
        return x / y
    else:
        "error! division by zero"

print("select operation")
print("1 add")      
print("2 substract")
print("3 multiply")
print("4 divide")  

choice = input("emter choice (1/2/3/4): ")

num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))

if choice == '1':
    print("result= ", add(num1, num2))
elif choice == '2':
    print("result=", substract(num1, num2))
elif choice == '3':
    print("result=", multiply(num1, num2))
elif choice ==  '4':
    print("result=", divide(num1, num2))
else:
    print("invalid user")





    
