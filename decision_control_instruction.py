# qty = int(input('Enter value of quantity: '))
# price = float(input('Enter value of price :'))
# if qty > 100:
#     dis = 10

# else:
#     dis = 0
# totext = qty * price - qty * price * dis/100
# print('total expenses = Rs.' + str(totext))


bs = int(input('Enter value of bs: '))
if bs > 1000:
    hra = bs *15/100
    da = bs * 95/100
    ca = bs * 10/100

else:
    hra = bs * 10/100
    da = bs * 10/100
    ca = bs * 10/100

gs = bs + da + hra + ca 
print('Gross salary = Rs.' + str(gs))
