from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(25), nullable=False)
    create_at = Column(DateTime, default=datetime.utcnow)

    workout_plans = relationship("WorkoutPlan", back_populates="user")
    progress_logs = relationship("ProgressLog", back_populates="user")


class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="workout_plans")
    workout_exercises = relationship("WorkoutExercise", back_populates="workout_plan")
    progress_logs = relationship("ProgressLog", back_populates="workout_plan")


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    instructions = Column(Text)
    image_url = Column(String(255))
    difficulty = Column(Integer)

    workout_exercises = relationship("WorkoutExercise", back_populates="exercise")


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id = Column(Integer, primary_key=True, autoincrement=True)
    workout_plan_id = Column(Integer, ForeignKey("workout_plans.id"), nullable=False)
    exercises_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    duration = Column(Integer)
    calories_burned = Column(Integer)
    heart_rate = Column(Integer)

    workout_plan = relationship("WorkoutPlan", back_populates="workout_exercises")
    exercise = relationship("Exercise", back_populates="workout_exercises")


class ProgressLog(Base):
    __tablename__ = "progress_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date)
    workout_plan_id = Column(Integer, ForeignKey("workout_plans.id"))
    total_calories = Column(Integer)
    total_duration = Column(Integer)
    avg_heart_rate = Column(Integer)

    user = relationship("User", back_populates="progress_logs")
    workout_plan = relationship("WorkoutPlan", back_populates="progress_logs")