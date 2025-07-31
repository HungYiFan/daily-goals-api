from sqlalchemy import Column, Integer, String, Boolean, Date
from .database import Base

class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    date = Column(Date)
    completed = Column(Boolean, default=False)
