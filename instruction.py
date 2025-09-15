i = 1
while i <= 3:
    j = 1
    while j <= 3:
        k = 1
        while k <= 3:
            if i == j or j == k or k == i:
                k += 1
                continue
            else:
                print(i, j, k)
            k += 1
        j += 1
    i+=1

i = 1
while i <= 3:
    p = float(input("Enter value of p:"))
    n = int(input("Enter value of n:"))
    r = float(input("Enter value of r:"))

    si = p * n * r / 100
    print("simple intreset = Rs." +str(si))
    i =i + 1


i = 1
while 1:
    print(i, end = " ")
    i+=1
    if i > 10:
        break