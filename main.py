while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            
            File = open("todos.txt", "r")
            todos = File.readlines()
            File.close()

            todos.append(todo)

            File = open("todos.txt", "w")
            File.writelines(todos)
            File.close()
        
        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo

        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        
        case "exit":
            break   