''' listing tasks
    adding a new task
    marking a task as completed
    archive (deleting all complete tasks)'''

def listing():

    with open("file.txt", "r") as file_handle: #####LISTÁZÁS
        lines=file_handle.read()
        print(lines+"\n")

def adding():

    with open("file.txt", "r") as file_handle: #####LISTÁZÁS
        lines=file_handle.read()
        print(lines+"\n")


    with open("file.txt", "a") as file_handle: #######HOZZÁADÁS
        b=input("Add a task:\n")
        file_handle.write(b + "\n")



    with open("file.txt", "r") as file_handle: #####LISTÁZÁS
        lines=file_handle.read()
        print("\n"+lines)








#with open("file.txt", "r") as file_handle: ####FELÜLÍRÁS
#    lines=file_handle.readlines()
    
#new_line=input("Add a new task: ")

#with open("file.txt", "w") as file_handle: ####FELÜLÍRÁS
#    for i in range(len(lines)):
#        if i==2:
#            file_handle.write(new_line + "\n")
#        else:
#            file_handle.write(lines[i])    ####FELÜLÍRÁS
            
def marking():

    with open("file.txt", "r") as file_handle: #####LISTÁZÁS
        lines=file_handle.readlines()
        linesr=file_handle.read()
        print(linesr+"\n")

    with open("file.txt", "w") as file_handle:

        for i in range(len(lines)):
            k=i+1
            print(str(k)+". " +lines[i])

        marked=int(input("\nMark a task with a number:"))
        wmark=[" "]
        mark=["X"]

        for j in range(len(lines)):
            if (j+1)==marked:
                file_handle.write(str(mark) + lines[j])
            else:
                file_handle.write(lines[j])

    with open("file.txt", "r") as file_handle: #####LISTÁZÁS
        lines=file_handle.readlines()

def remove():

    with open("file.txt", "r") as file_handle:
            lines=file_handle.readlines()



    with open("file.txt", "w") as file_handle:
        for i in range(len(lines)):
            row=lines[i]
            for j in range(len(row)):
                if lines[i][2]!="X":
                    file_handle.write(lines[i][j])

while True:
    
    inp=int(input("1.list\n2.Add\n3.Mark\n4.remove\n"))

    if inp==1:
        listing()
    elif inp==2:
        adding()
    elif inp==3:
        marking()
    elif inp==4:
        remove()
    else:
        break