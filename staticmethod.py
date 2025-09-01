# class car:
#     def __init__(self, type):
#         self.type = type

#         @staticmethod
#         def start():
#             print("car started..")

#         @staticmethod
#         def stop():
#             print("car stopped..")

# class Toyotacar(car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = Toyotacar("fortuner", "electric")

# print(car1. type)

# class person:
#     name = "anonymous"

    # def changeName(self, name):
    #     self.__class__.name = "mithlesh"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name


# p1 = person()
# p1.changeName("mithlesh")
# print(p1.name)
# print(person.name)


class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self. math = math
    
    @property
    def percentage(self):
        return  str((self.phy + self.chem + self.math) / 3) + '%'



stu1 = student(90, 80, 70)
print(stu1.percentage)

stu1.phy  = 86
print(stu1.percentage)










        
