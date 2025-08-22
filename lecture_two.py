str1 = "this is a string"
str2 = 'mangalayatan university'
str3 = """this is a string"""

print(str2)

str1 = "this is a string.\nwe are creating it in python."
print(str1)

str1 = "managalayatan"
str2 = "collage"
final_str = str1+str2
print(final_str)


str1 = "mangalayatan"
len1 = len(str1)
print(len1)

str2 = "collage"
len2 = len(str2)
print(len2)


final_str = str1 +" "+ str2
print(final_str)
print(len(final_str))

str = "apna college"
print(str[:4]) #[0:4]
print(str[5:]) #[5: len(str)]


str = "apple"
print(str[-5])

str = "i am studying from python apna college"
print(str.endswith("app"))

str = "i studying python from apnacollege"
str = str.capitalize()
print(str)

str = "i am studying python from apna college"
print(str.replace("python", "javascript"))

str = "i am from studying python from apna college"
print(str.find("from"))

str = "i am from studying python from apnacollege"
print(str.count("o"))

name = input("enter your name:")
print("len of your name", len(name))

str = "hii ,$iam the $ symbol $99.99"
print(str.count("$"))



light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

print("end of code")


age = 16

if(age >= 18):
    print("can vote")

a = int(input("enter first number:"))
b = int(input("enter second mumber:"))
c = int(input("enter third number:"))
d = int(input("enter fourth number:"))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
elif(c >= d):
    print("third number is largest", c)
else:
    print("forth number is largest", d)

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
d = int(input("enter fourth number:"))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
elif(c >= d):
    print("third number is largest:", c)
else:
    print("fourth number is largest" ,d)


x = int(input("enter number:"))

if(x % 7 == 0):
    print("multiple of 8")
else:
    print("not a multiple")

str1 = 'mangalayatan university'
str2 = """mangalayatan university"""
str3 = "mangalayatan univertsity"

print(str2)

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
d = int(input("enter fourth number:"))

if ( a >= b and a >= c):
    print("first number is largest", a)
elif( b >= c):
    print("second numner is largest", b)
elif( c >= d):
    print("third number is largest", c)
else:
    print("fourth number is largest", d)

marks1 = 60.5
marks2 = 65.5
marks3 = 50.5
marks4 = 70.5
marks5 = 75

print(marks4)
print(type(marks2))
print(type(marks5))


marks = [45.5, 25.5, 45.5, 50.5, 45.7 ]
print(marks)
print(len(marks))
print(type(marks))

marks = [95, 65, 75, 86,  90]
print(marks[-3:-1])

a = int(input("enter first number:"))
b = int(input("enter sercond number:"))
c = int(input("enter third numberl:"))
d = int(input("enter fourth number:"))

if(a >= b and b >= c):
    print("first number is largest")
elif(b >= c):
    print("second number is largest")
elif(c >= d):
    print("third number is largest")
else:
    print("fourth number is largest")


    








