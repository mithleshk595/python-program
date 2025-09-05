class complex:
    def __init__(self, real, img,):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, name2):
        newReal = self.real + num2. real
        newImg = self.img + num2.img
        return complex(newReal, newImg)
    
    def __sub__(self, name2):
        newReal = self.real - num2.img
        newImg = self.img - num2.img
        return complex(newReal, newImg)


num1 = complex(1, 3)
num1.shownumber()

num2 = complex(4, 6)
num2.shownumber()


num3 = num1 - num2
num3.shownumber()

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) + self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    

c1 = circle(21)
print(c1.area())
print(c1.perimeter())


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept= ", self.dept)
        print("salary= ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age,):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75.000")

engg1 = Engineer("Elon mask", 40)
engg1.showDetails()


class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price
    

ord1 = order("chips", 20)
ord2 = order("tea", 15)


print(ord1 > ord2)






