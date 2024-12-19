from sqlalchemy.orm import Session
from models import User, WorkoutPlan, Exercise, WorkoutExercise, ProgressLog
from schemas import (
    UserCreate,
    WorkoutPlanCreate,
    ExerciseCreate,
    WorkoutExerciseCreate,
    ProgressLogCreate,
)

# CRUD operations for User
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# CRUD operations for WorkoutPlan
def get_workout_plan(db: Session, plan_id: int):
    return db.query(WorkoutPlan).filter(WorkoutPlan.id == plan_id).first()


def get_workout_plans_by_user(db: Session, user_id: int):
    return db.query(WorkoutPlan).filter(WorkoutPlan.user_id == user_id).all()


def create_workout_plan(db: Session, plan: WorkoutPlanCreate):
    db_plan = WorkoutPlan(
        user_id=plan.user_id, name=plan.name, description=plan.description
    )
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan


# CRUD operations for Exercise
def get_exercise(db: Session, exercise_id: int):
    return db.query(Exercise).filter(Exercise.id == exercise_id).first()


def get_all_exercises(db: Session):
    return db.query(Exercise).all()


def create_exercise(db: Session, exercise: ExerciseCreate):
    db_exercise = Exercise(
        name=exercise.name,
        instructions=exercise.instructions,
        image_url=exercise.image_url,
        difficulty=exercise.difficulty,
    )
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


# CRUD operations for WorkoutExercise
def get_workout_exercise(db: Session, workout_exercise_id: int):
    return db.query(WorkoutExercise).filter(WorkoutExercise.id == workout_exercise_id).first()


def get_workout_exercises_by_plan(db: Session, plan_id: int):
    return db.query(WorkoutExercise).filter(WorkoutExercise.workout_plan_id == plan_id).all()


def create_workout_exercise(db: Session, workout_exercise: WorkoutExerciseCreate):
    db_workout_exercise = WorkoutExercise(
        workout_plan_id=workout_exercise.workout_plan_id,
        exercises_id=workout_exercise.exercises_id,
        duration=workout_exercise.duration,
        calories_burned=workout_exercise.calories_burned,
        heart_rate=workout_exercise.heart_rate,
    )
    db.add(db_workout_exercise)
    db.commit()
    db.refresh(db_workout_exercise)
    return db_workout_exercise


# CRUD operations for ProgressLog
def get_progress_log(db: Session, log_id: int):
    return db.query(ProgressLog).filter(ProgressLog.id == log_id).first()


def get_progress_logs_by_user(db: Session, user_id: int):
    return db.query(ProgressLog).filter(ProgressLog.user_id == user_id).all()


def create_progress_log(db: Session, log: ProgressLogCreate):
    db_log = ProgressLog(
        user_id=log.user_id,
        date=log.date,
        workout_plan_id=log.workout_plan_id,
        total_calories=log.total_calories,
        total_duration=log.total_duration,
        avg_heart_rate=log.avg_heart_rate,
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log