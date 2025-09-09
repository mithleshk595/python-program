# import random

# a = []
# i = 1
# while i <= 15:
#     num = random.randint(10, 100)
#     a.append(num)
#     i += 1
    
#     print(a)

    
# for num in a:
#     if num > 20 and num < 50:
#         a.remove(num)

# print(a)

mat1 = [[1, 2, 3, 4], [5, 6, 7 ,8], [9, 10, 11, 12]]
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11 ,12]]
mat3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# iterate through rows 
for i in range(len(mat1)):
    # iterate through colonms
    for j in range(len(mat1[0])):
        mat3[i][j] = mat1[i][j] + mat2[i][j]

print(mat3)



