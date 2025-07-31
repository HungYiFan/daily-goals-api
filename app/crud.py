from sqlalchemy.orm import Session
from . import models, schemas

def create_goal(db: Session, goal: schemas.GoalCreate):
    db_goal = models.Goal(**goal.dict())
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

def get_goals_by_date(db: Session, goal_date):
    return db.query(models.Goal).filter(models.Goal.date == goal_date).all()

def complete_goal(db: Session, goal_id: int):
    goal = db.query(models.Goal).get(goal_id)
    goal.completed = True
    db.commit()
    return goal

def delete_goal(db: Session, goal_id: int):
    goal = db.query(models.Goal).get(goal_id)
    db.delete(goal)
    db.commit()

