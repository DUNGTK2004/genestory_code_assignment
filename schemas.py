from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum

# --------------------- Task Schemas ---------------------
class TaskBaseSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None  # "Low", "Medium", "High"
    is_done: bool = False

class TaskCreate(TaskBaseSchema):
    ...

class TaskUpdate(TaskBaseSchema):
    ...

class Task(TaskBaseSchema):
    id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

# --------------------- Prediction Schemas ---------------------
class ModelName(str, Enum):
    LogisticRegression = "LogisticRegression"
    MultinomialNB = "MultinomialNB"
    ComplementNB = "ComplementNB"

class PredictRequest(BaseModel):
    title: str
    description: Optional[str] = None
    auto_assign: bool = True
    model_name: ModelName = ModelName.LogisticRegression
