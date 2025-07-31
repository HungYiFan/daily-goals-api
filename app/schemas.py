from pydantic import BaseModel
from datetime import date

class GoalCreate(BaseModel):
    description: str
    date: date

class GoalOut(GoalCreate):
    id: int
    completed: bool

    class Config:
        orm_mode = True
