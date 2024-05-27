from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import models
from database import create_table

app = FastAPI()

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskUpdate(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.on_event("startup")
def startup():
    create_table()

@app.post("/tasks/", response_model=int)
def create_task(task: Task):
    task_id = models.add_task((task.title, task.description, task.completed))
    return task_id

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    tasks = models.get_tasks()
    return [Task(title=row[1], description=row[2], completed=row[3]) for row in tasks]

@app.put("/tasks/", response_model=None)
def update_task(task: TaskUpdate):
    models.update_task((task.title, task.description, task.completed, task.id))
    return None

@app.delete("/tasks/{task_id}", response_model=None)
def delete_task(task_id: int):
    models.delete_task(task_id)
    return None
