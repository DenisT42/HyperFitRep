from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP, Date
from sqlalchemy.orm import relationship
from database import Base

# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(25), nullable=False)  # Use hashed passwords in production
    create_at = Column(TIMESTAMP)

    # Relationships
    workout_plans = relationship("WorkoutPlan", back_populates="user", cascade="all, delete")
    progress_logs = relationship("ProgressLog", back_populates="user")

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# Workout Plan Model
class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP)

    # Relationships
    user = relationship("User", back_populates="workout_plans")
    workout_exercises = relationship("WorkoutExercise", back_populates="workout_plan", cascade="all, delete")
    progress_logs = relationship("ProgressLog", back_populates="workout_plan")


# Exercise Model
class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    instructions = Column(Text)
    image_url = Column(String(255))
    difficulty = Column(Integer)

    # Relationships
    workout_exercises = relationship("WorkoutExercise", back_populates="exercise")


# Workout Exercise Model
class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id = Column(Integer, primary_key=True, index=True)
    workout_plan_id = Column(Integer, ForeignKey("workout_plans.id", ondelete="CASCADE"), nullable=False)
    exercises_id = Column(Integer, ForeignKey("exercises.id", ondelete="CASCADE"), nullable=False)
    duration = Column(Integer)
    calories_burned = Column(Integer)
    heart_rate = Column(Integer)

    # Relationships
    workout_plan = relationship("WorkoutPlan", back_populates="workout_exercises")
    exercise = relationship("Exercise", back_populates="workout_exercises")


# Progress Log Model
class ProgressLog(Base):
    __tablename__ = "progress_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False)
    workout_plan_id = Column(Integer, ForeignKey("workout_plans.id", ondelete="CASCADE"))
    total_calories = Column(Integer)
    total_duration = Column(Integer)
    avg_heart_rate = Column(Integer)

    # Relationships
    user = relationship("User", back_populates="progress_logs")
    workout_plan = relationship("WorkoutPlan", back_populates="progress_logs")