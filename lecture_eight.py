# class Student:
#     name = "john"

# s1 = Student()
# print(s1.name)

# s2  = Student()
# print(s2.name)


# class car:
#     color = "blue"
#     model = "bmw"

# car1 = car()
# print(car1.color)
# print(car1.model)


class student:
    name = "mithlesh"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


        print("adding new student in databse..")
s1 = student("mithlesh", 90)
print(s1.name, s1.marks) #mithlesh

s2 = student("john", 80)
print(s2.name, s2.marks) #john
 

