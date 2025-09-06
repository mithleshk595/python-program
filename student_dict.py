students = {554 : 'Mithlesh', 350 : 'Manish', 395 : 'Ramesh', 400 : 'Rakesh'}

rollno = int(input("Enter roll no: "))
name = students.get(rollno, 'student')
print(f'congrulation {name}!')
rollno = int(input("Enter roll number :"))

name = students.get(rollno, 'student')
print("congralution {name}!")