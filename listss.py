# create a list of 5 odd number
a = [1, 3, 5, 7, 9]
print(a)

#create a listt of 5 even numbers
b = [2, 4, 6, 8, 10]
print(b)

#combine the two lists
a = a + b
print(a)

# add prime number 11, 17, 29 at the beginning of the combined list 
a = [11, 17, 29] + a
print(a)

# report how many elements are present in the list
num = len(a)
print(num)

#replace last 3 numbers in the list with 100, 200, 300
a[num-3:num]=[100, 200, 300]
print(a)

#delete all the numbers in the list
a[:] = []
print(a)

#delete the list
del a


# stack - LIFO  list
s = [] #empty stack

#push elements on stack
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)
print(s)

#pop elements  from back
print(s.pop())
print(s.pop())
print(s.pop())
print(s)