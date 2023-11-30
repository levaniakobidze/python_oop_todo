import random

class Todo():
    def __init__(self):
        self.tasks = []
        
    def add_task(self,task):
        self.tasks.append(task)
        print(f"Task '{task} added'")
        
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task} deleted'")
        else:
            print("Task not found.")   
            
    def view_all_tasks():
        if self.tasks:
            print("Your tasks:")
            for index,task in enumerate(self.tasks,start=1):
                print(f"{index}, {task}")
            else:
                print("No tasks yet.")
        
        
     
if __name__ == "__main__":
    todo_app = Todo()   
  