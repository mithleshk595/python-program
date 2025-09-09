# result = divmod(17, 3)
# print(result)
# t = (17, 3)
# result = divmod(*t)
# print(result)

# tpl = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# a, b, c, d, e, f, g, h, i, j = tpl
# print(tpl)
# print(a, b ,c ,d ,e, f, g, h, i, j)
# x, y = tpl
# print(x, y,)
# i, * j = tpl
# print(i, j)

lst = ["Shobha", "Nishu", "Sudha", ("Suresh"), ("Rajesh"), "Radha"]
boys = 0
girls = 0
for ele in lst:
    if isinstance(ele, tuple):
        boys +=1
    else:
        girls +=1

print("Boys= ", boys, "girl= ", girls)

