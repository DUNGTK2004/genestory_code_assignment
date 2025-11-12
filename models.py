from database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(String, nullable=True)
    is_done = Column(Boolean, nullable=True, default=False)
    predictions = relationship("PredictionLog", back_populates="task")

class PredictionLog(Base):
    __tablename__ = "prediction_log"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    predicted_priority = Column(String, nullable=False)
    mlflow_run_id = Column(String, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    task = relationship("Task", back_populates="predictions")
