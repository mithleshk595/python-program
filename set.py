a ={10, 20, 30 ,40, 50, 60, 70}
b ={ 33, 44, 51, 10, 20, 50, 33, 51}

print(a | b)
print(a & b)
print(a - b)
print(b - a)
print( a ^ b)
print(a <= b)
print(a >= b)

a = {1, 2, 3, 4 ,5 ,6, 7}
b = {1, 2, 3, 4, 5, 6, 7}
c = {1, 2 ,3, 4, 5, 6, 7}
d = {1, 2, 3, 4, 5, 6, 7}
e = {3, 4, 1, 0, 2, 5, 8, 9}
print(a)
a &= e
print(b)
c -= e
print(c)
d ^= e
print(d)

