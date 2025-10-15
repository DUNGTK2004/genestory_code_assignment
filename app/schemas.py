from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class TaskBaseSchema(BaseModel):
    title: str = None
    description: str = None
    is_done: bool = False

class TaskCreate(TaskBaseSchema):
    pass

class TaskUpdate(TaskBaseSchema):
    pass

class Task(TaskBaseSchema):
    id: int
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
    


