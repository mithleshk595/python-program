# class Student:
#     college = "ABC college"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in databse")

# s1 = Student("mithlesh", 90)
# print(s1.name, s1.marks, s1.college)


# class Student:
#     college = "ABC college"   # class variable

#     def __init__(self, name, marks):  # constructor
#         self.name = name
#         self.marks = marks

#     def welcome(self):   # method 1
#         print("Welcome student,", self.name)

#     def get_marks(self):  # method 2
#         return self.marks


# s1 = Student("Karan", 90)
# s1.welcome()                # method call (chhota 'w')
# print(s1.get_marks())       # prints marks

    
# class Student:
#     def __init__(self, name, marks): 
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("hello")


#     def get_avg(self):
#         total = 0
#         for value in self.marks:
#             total += value
#         print("Hi", self.name, "your avg score is:", total / len(self.marks))



# s1 = Student("mithlesh", [90, 98, 99])
# s1.get_avg()

# s1.name = "john"
# s1.get_avg()
# s1.hello()



# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):   # ye __init__ ke bahar hona chahiye
#         self.clutch = True
#         self.acc = True
#         print("Car started..")


# car1 = Car()
# car1.start()

# class Account:
#     def __init__(self, bal, acc):
#         self.bal = bal
#         self.acc = acc
    
#     #debit method
#     def debit(self, amount):
#         self.balance -=  amount
#         print("RS", amount, "was debited")
#         print("total balance = ", self.get_balance())


#     def credit(self, amount):
#         self.balance += amount
#         print("RS", amount, "was debited")
#         print("total balance = ", self.get_balance())
        


#     def get_balance(self):
#         return self.balance

        
    

# acc1 = Account(1000, "12345")
# acc1.debit(500)
# acc1.credit(2000)
# acc1.credit(4000)


class Account:
    def __init__(self, balance, acc):
        self.balance = balance   # ✅ consistent naam
        self.acc = acc
    
    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total balance =", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance =", self.get_balance())
        
    # get balance
    def get_balance(self):
        return self.balance


# object create
acc1 = Account(1000, "12345")
acc1.debit(500)
acc1.credit(2000)
acc1.credit(4000)

















