from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Integer
from sqlalchemy.sql import func

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_done = Column(Boolean, nullable=True, server_default='False')