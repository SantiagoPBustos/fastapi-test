from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(    
    title="Mi API Personalizada",
    description="Esta es una descripción personalizada de mi API",
    version="1.0.5",
    )

# Model para las tareas
class Task(BaseModel):
    id: int
    title: str
    description: str

# Base de datos de tareas (temporal)
tasks_db = []

# Operación para crear una tarea
@app.post("/tasks/", tags = ["Reportes"], response_model=Task)
def create_task(task: Task):
    return task

# Operación para obtener todas las tareas
@app.get("/tasks/", response_model=list[Task])
def read_tasks():
    return tasks_db

# Operación para obtener una tarea por ID
@app.get("/get_tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tasks_db[task_id]

from enum import Enum
# Datos de ejemplo (en una aplicación real, estos datos vendrían de una base de datos)
class RecordLimit(Enum):
    ten = 10
    twenty = 20
    fifty = 50

# Datos de ejemplo (en una aplicación real, estos datos vendrían de una base de datos)
sample_data = list(range(1, 101))  # Una lista de números del 1 al 100

@app.get("/get_records/")
async def get_records(limit: RecordLimit = RecordLimit.twenty):
    """
    Obtén una lista de registros con opciones de filtrado.
    """
    records = sample_data[limit.value]
    return {"records": records}