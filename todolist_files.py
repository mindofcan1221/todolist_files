from datetime import date
current_date=date.today()

#function to accept tasks
def task_list(filename,tasks):
    count = 0
    myfile = open(filename,'w')
    print("\n Enter your tasks.")
    print("Enter 'exit' to stop")
    while True:
        yourtask = input(f"Enter your task {len(tasks)+1 }:")
        if yourtask.lower()=='exit':
            print("You can come next and fill their status")
            break
        else:
                tasks[yourtask] = 'unspecified'

    #write the date and tasks on task.txt file
    myfile.write("Date:"+str(current_date))
    myfile.write("\n"+str(tasks)) 
    print("Tasks have been saved to", filename)  

#function to accept status of tasks
def status_list(filename):
    myfile = open(filename,'r')
    list_str = myfile.readlines()
    taskdic= eval(list_str[1])
    taskdickeys=list(taskdic.keys())
    count = 0
    print("\n Enter status of your tasks as complete/incomplete.")
    print("Enter 'exit' to stop")
    while True:
        yourstatus = input("Status of task "+taskdickeys[count]+":")
        if yourstatus.lower()=='exit':
            break
        else:
            taskdic[taskdickeys[count]] = yourstatus
            count+=1
            if count == len(taskdic): break
    
    '''while count<len(taskdic):
        tasks.append("unspecified")
        count+=1''' 

    myfile=open(filename,'a')
    myfile.write("\n"+str(taskdic))
    print("The status of your work are now updated")