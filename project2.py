import random
import string

pass_len = 12
charValues = string.ascii_letters + string.punctuation + string.digits

#list comprehension  [function for i in range(n):]

password ="".join ([random.choice(charValues) for i in range(pass_len)])

# password  = ""
# for i in range(pass_len):
#     password  += random.choice(charValues)


# print("your random password is :", password)     

print("your random password listg", password)



