import operator

d = {"oil" : 230,  "clip" : 150, "stud" : 175, "nut" : 35 }
print("original dictionary :", d)

#sorting by key
d1 = sorted(d.items())
print("asc.order by key :", d1)
d2 = sorted(d.items(), reverse= True)
print("des.order by key ", d2)

#sorting by value

d1 = sorted(d.items(), key = operator.itemgetter(1))
print("asc.order by value :", d1)
d2 = sorted(d.items(), key= operator.itemgetter(1), reverse= True)
