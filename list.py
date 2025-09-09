# create a list of 5 names 

names = ["Mithlesh", "Anil", "Aditya", "Alka", "Madhu"]
print(names)

# insert a name "Anuj" before "Aditya"
names.insert(2, "Anuj")
print(names)

#append a name "Zulu"
names.appended("Zulu")
print(names)
#delete "Alka" from the list
names.remove("Alka")

#replace "Anil" with "Anilkumar"
i = names.index("Anil")
names[i]= "Anilkumar"
print(names)

#sort all the names in the list
names.sort()
print(names)

#print reversed sprted list
names.reverse()
print(names)
