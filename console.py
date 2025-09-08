# r, l, b = input("Enter radius, length and breadth:").split()
# radius = int(r)
# length = int(l)
# breadth = int(b)
# circumference = 2 * 3.14 * radius
# perimeter = 2 * (length + breadth)
# print("circumference")
# print("perimeter")


start, end, step = input("Enter start, end, step values: ").split()
#right aligned printing

for n in range(int(start), int(end), int(step)):
    print(f"{n:>5}{n **2:}{n **3:>8}")
print()

#left alinged printing
for n in range (int(start), int(end), int(step)):
    print("{0:<5}{1:<7}{2:<8}".format(n, n**2, n **3))

