from fastapi import FastAPI
from pydantic import BaseModel, Field
tasks = []
app = FastAPI()
class Task(BaseModel):
    title:str
    description:str
    priority:str
    is_completed:bool = False
@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    if not task.title.strip():
        return {"message": "Task title cannot be empty"}
    return {"message": "Task created successfully", "task": task}
@app.get("/tasks")
def get_all_tasks():
    return {"message": "List of all tasks", "total_tasks": len(tasks), "tasks": tasks}
@app.put("/task/{position}")
def update_task(position:int , updated_task: Task):
    if 0<= position < len(tasks):
        if not updated_task.title.strip():
            return {"message": "Task title cannot be empty"}
        tasks[position] = updated_task
        return {"message": "Task updated successfully", "task": updated_task}
@app.delete("/task/{position}")
def delete_task(position:int):
    if 0<= position < len(tasks):
        deleted_task = tasks.pop(position)
        return {"message": "Task deleted successfully", "task": deleted_task}    
    

