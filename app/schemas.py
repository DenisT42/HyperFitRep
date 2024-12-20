from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime, date

# User Schemas
class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    create_at: datetime

    class Config:
        orm_mode = True


# WorkoutPlan Schemas
class WorkoutPlanBase(BaseModel):
    name: str
    description: Optional[str] = None


class WorkoutPlanCreate(WorkoutPlanBase):
    user_id: int


class WorkoutPlanResponse(WorkoutPlanBase):
    id: int
    user_id: int
    created_at: datetime


    class Config:
        orm_mode = True


# Exercise Schemas
class ExerciseBase(BaseModel):
    name: str
    instructions: Optional[str] = None
    image_url: Optional[str] = None
    difficulty: Optional[int] = None


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseResponse(ExerciseBase):
    id: int

    class Config:
        orm_mode = True


# WorkoutExercise Schemas
class WorkoutExerciseBase(BaseModel):
    duration: Optional[int] = None
    calories_burned: Optional[int] = None
    heart_rate: Optional[int] = None


class WorkoutExerciseCreate(WorkoutExerciseBase):
    workout_plan_id: int
    exercises_id: int


class WorkoutExerciseResponse(WorkoutExerciseBase):
    id: int
    workout_plan_id: int
    exercises_id: int

    class Config:
        orm_mode = True


# ProgressLog Schemas
class ProgressLogBase(BaseModel):
    date: date
    total_calories: Optional[int] = None
    total_duration: Optional[int] = None
    avg_heart_rate: Optional[int] = None


class ProgressLogCreate(ProgressLogBase):
    user_id: int
    workout_plan_id: Optional[int] = None


class ProgressLogResponse(ProgressLogBase):
    id: int
    user_id: int
    workout_plan_id: Optional[int] = None

    class Config:
        orm_mode = True