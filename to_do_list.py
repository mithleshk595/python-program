# Simple To-Do List Program

tasks = []

# while True:
#     print("\n--- TO-DO LIST MENU ---")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Delete Task")
#     print("4. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         task = input("Enter new task: ")
#         tasks.append(task)
#         print("Task added!")

#     elif choice == "2":
#         if not tasks:
#             print("No tasks yet.")
#         else:
#             print("\nYour Tasks:")
#             for i, t in enumerate(tasks, 1):
#                 print(f"{i}. {t}")

#     elif choice == "3":
#         if not tasks:
#             print("No tasks to delete.")
#         else:
#             num = int(input("Enter task number to delete: "))
#             if 1 <= num <= len(tasks):
#                 deleted = tasks.pop(num-1)
#                 print(f"Deleted: {deleted}")
#             else:
#                 print("Invalid task number.")

#     elif choice == "4":
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice. Try again.")


# # Simple To-Do-list program

# tasks = []

# while True:
#     print("\n------ TO-DO LIST MENU------")
#     print("1. Add task")
#     print("2. viem task")
#     print("3. delete task")
#     print("4. exit")

#     choice = input("enter choice: ")

#     if choice == "1":
#         task = input("enter  new task:")
#         tasks.append(task)
#         print("task added!")
    
#     elif choice == "2":
#         if not task:
#             print("no tasks yet.")
#         else:
#             print("\nyour tasks")    
#             for i, t in enumerate(task, 1):
#                 print(f"{i}. {t}")
    
#     elif choice == "3":
#         if not tasks:
#             print("no task to delete.")
#         else:
#             num = int(input("enter task to number delete: "))
#             if 1 <= num <= (tasks):
#                 deleted = tasks.pop(num-1)
#                 print(f"deleted: {deleted}", )
#             else:
#                 print("invalid task number.")
#     elif choice == "4":
#         print("goodbye!")
#         break
#     else:
#         print("invalid choice try again.")

# # simple program to- do list

# tasks = []

# while True:
#     print("\n ----- TO-DO LIST MENU-----")
#     print("1. Add task")
#     print("2. viem task")
#     print("3. delete task")
#     print("4. exit")

#     choice =input("enter choice :")

#     if choice == "1":
#         task = input("enter new tasks")
#         tasks.append(task)
#         print("task adeded")

#     elif choice == "2":
#         if not task:
#             print("no task yet.")
#         else:
#             print("\nyour task")
#             for i, t in enumerate(task, 1):
#                 print(f"{i}. {t}")
    
#     elif choice == "3":
#         if not tasks:
#             print("no taks delete.")
#         else:
#             num = int(input("enter task to number delete:"))
#             if 1 <= num <= (tasks):
#                 deleted= tasks.pop(num-1)
#                 print(f"deleted: {deleted}")
#                 print("invalid task number.")

        
#     elif choice == "4":
#         print("goodbye")
#         break
#     else:
#         print("invalid choice try again")

    
        
# tasks = []

# while True:
#     print("-----TO-DO LIST MENU-----")
#     print("1. Add tasks")
#     print("2. viem tasks")
#     print("3. delete tasks")
#     print("4. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         task = input("Enter new tasks:")
#         tasks.appended(tasks)
#         print("task added!")
    
#     elif choice == "2":
#         if not task:
#             print("No taske yet..")
#         else:
#             print("\nyour task")
#             for i , t in enumerate(task, 1):
#                 print(f"{i}, {t}")

#     elif choice == "3":
#         if not task:
#             print("No taks delete:")
#         else:
#             num = int(input("enter  task to number delete:"))
#             if 1 <= num <= (task):
#                 deleted = tasks.pop(num-1)
#                 print(f"deleted: {deleted}")
            
#     elif choice == "4":
#         print("Goodbye:")
#         break
#     else:
#         print("invalid choice try again")

tasks = []

while True:
    print("-----TO-DO LIST MENU-----")
    print("1. Add tasks")
    print("2. viem tasks")
    print("3. delete tasks")
    print("4. Exit")

    choice = input("Enter choice :")

    if choice == "1":
        tasks = input("Enter new tasks")
        tasks.appended(tasks)
        print("task added!")

    elif choice == "2":
        if not tasks:
            print("no task yet.")
        else:
            print("\nYour task." )
            for i, t in enumerate(tasks, 1):
                print(f"{i}, {t}")

    elif choice == "3":
        if not tasks:
            print("not task delete:")
        else:
            num = int(input("Enter task to number delete :"))
            if 1 <= num <= (tasks):
                deleted = tasks.pop(num-1)
                print(f"deleted {deleted}")

    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("invalid choice try again")
    



def add(x,y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divison(x, y):
    if y !=0:
        return x / y
    
    print("select operation:")
    print("1 Add")
    print("2 substract")
    print("3 mutiply")
    print("4 divison")


    

choice = input("Enter your choice(1/2/3/4): ")


num1 = input("Enter first number:")
num2 = input("Enter second number:")

if choice == "1":
    print("Result= ", add(num1, num2))

elif choice == "2":
    print("Result= ", (num1, num2))

elif choice == "3":
    print("Result= ", (num1, num2))

elif choice == "4":
    print("Result =", (num1, num2))

else:
    print("invalid user")



# tasks = []

# while True:
#     print("----TO-DO LIST MENU----")
#     print("1. Add tasks")
#     print("2. Viem tasks")
#     print("3. Delete tasks")
#     print("4. Exit")

#     choice = input("Enter choice:")
    
#     if choice == "1":
#         tasks = input("Enter new tasks")
#         tasks.appended(tasks)
#         print("task added!")
    
#     elif choice == "2":
#         if not tasks:
#            print("No tasks yet.")
#         else:
#             print("\nYour task:")
#             for i , t in enumerate(tasks):
#                 print(f"{i}, {t}")
    
#     elif choice == "3":
#         if not tasks:
#             print("not tasks delete:")
#         else:
#              num = int(input("enter task to number delete:"))
#              if 1 <= num <= (tasks):
#                  deleted = tasks.pop(num-1)
#                  print(f"{deleted}, {deleted}")

#     elif choice == "4":
#         print("Goodbye!")
#         break
#     else:
#         print("invalid number try again")






        


        





