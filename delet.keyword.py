# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 =Student("john")
# print(s1.name)
# del s1.name

# print("after delecting the name attribute")


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.acc_pass)

# acc1 = Account(12345, "mypassword")
# print(acc1.acc_no)
# print(acc1.acc_pass)
# print(acc1.reset_pass())

# class person:
#     __name = "mithlesh"

#     def __hello(self):
#         print("hello person")

#     def welcome(self):
#         self.__hello()

# p1 = person()

# print(p1.welcome())"
class car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Toyotacar(car):
    def __init__(self, brand):
        self.brand = brand

class fortuner(Toyotacar):
    def __init__(self, type):
        self.type = type

car1 = fortuner("diesel")
car1.start()


class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"
    
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)





