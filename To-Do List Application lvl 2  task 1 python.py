import json

try:
    with open("tasks.json","r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []
    
while True:
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")
    choice = input("enter your choice")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({
            "task" : task,
            "done" : False
                     })
        print("task added successfully")

    elif choice == "2":
        if not tasks:
            print("no task found")
        else:
            for task in tasks:
                if task["done"]:
                    status = "Done"
                else:
                    status = "Pending"
                print(task["task"], "-", status)
    elif choice == "3":
        if not tasks:
            print("no task found")
        else:
            delete_task = int(input("enter task no to delete"))
            if 1 <= delete_task <= len(tasks):
                tasks.pop(delete_task - 1)
                print("task deleted Sucessfully")
            else:
                print("task doesnot exist")
    elif choice == "4":
        if not tasks:
            print("no task found")
        else:
            done_task = int(input("enter task no to mark as done"))
            if 1 <= done_task <= len(tasks):
                tasks[done_task - 1]["done"] = True
                print("task marked as done")
            else:
                print("task doesnot exist")
    elif choice == "5":
        with open("tasks.json","w") as file:
            json.dump(tasks, file)
        print("tasks saved sucessfully")
        break
