tasks = []

while True:
    print("\n---- TO-DO LIST MENU-----")
    print("1. Add tasks")
    print("2. Viem tasks")
    print("3. Delete tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        tasks = input("Enter new tasks:")
        tasks.append(tasks)
        print("tasks addded:")
    
    elif choice =="2":
        if not tasks:
            print("no tasks yet.")
        else:
            print("\nyour tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}, {t}")
    
    elif choice == "3":
        if not tasks:
            print("no tasks to delete.")
        else:
            num = int(input("enter tasks to number delete: "))
            if 1 <= num <= len(tasks):
                delete = tasks.pop(num-1)
                print(f"deleted: {delete}")
            else:
                print("invalid tasks number.")
    
    elif choice == "4":
        print("goodbye!")
        break
    else:
        print("invalid choice try again.")
        

            

