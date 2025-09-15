# print(1 + 2) #3
# print(type(1))


# print("apna" + "college") #contance
# print(type("apna"))

# print([1, 2, 3] + [4, 5, 6]) #merge 
# print(type([1, 2, 3]))


class complex:
    def __init__(self, real, img,):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self):
        return f"{self.real}i + {self.img}j"


num1 = complex(1, 3)
num1.shownumber()

num2 = complex(4, 6)
num2.shownumber()


num3 = num1.add(num2)
print(num3)








