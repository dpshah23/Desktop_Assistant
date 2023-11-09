import csv
import os
import speak as ap

def createtask(taskname,date):
    notdone="notdone"
    file_exists = os.path.exists("task.csv")
    with open("task.csv", mode='a', newline='') as file:
        Filedname = ['task_name', 'date', 'status']
        writer = csv.DictWriter(file, fieldnames=Filedname)
        if not file_exists:
            writer.writeheader()
            writer.writerow(
                {'task_name': taskname, 'date': date, 'status': notdone})
            file.close()

def markdone(taskname,date):
    with open('task.csv', 'r') as f1:
                 data = f1.readlines()
                 for row in data:
                     if taskname and date in row:
                         
                         data[i] = data[i].replace("Not Done", "Done")
                         ap.speak(f"Task Marked Done Successfully with Task Name : {taskname} and date : {date}")
                         with open('task.csv', 'w') as f1:
                            f1.writelines(data)
                         
                         return
                     i = i+1
 
                 
