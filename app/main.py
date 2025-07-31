from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base
from datetime import date

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/goals/")
def create_goal(goal: schemas.GoalCreate, db: Session = Depends(get_db)):
    return crud.create_goal(db, goal)

@app.get("/goals/{goal_date}")
def get_goals(goal_date: date, db: Session = Depends(get_db)):
    return crud.get_goals_by_date(db, goal_date)

@app.put("/goals/{goal_id}/complete")
def complete(goal_id: int, db: Session = Depends(get_db)):
    return crud.complete_goal(db, goal_id)

@app.delete("/goals/{goal_id}")
def delete(goal_id: int, db: Session = Depends(get_db)):
    return crud.delete_goal(db, goal_id)
