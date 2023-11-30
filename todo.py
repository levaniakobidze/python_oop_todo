import random

class Todo():
    def __init__(self):
        self.tasks = []
        
    def add_task(self,task):
        self.tasks.append(task)
        print(f"Task '{task} added'")
        
     
if __name__ == "__main__":
    todo_app = Todo()   
