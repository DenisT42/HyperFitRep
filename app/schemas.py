from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime, date


# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=25, description="Password must be between 8 and 25 characters")


class UserResponse(UserBase):
    id: int
    create_at: Optional[datetime]

    class Config:
        orm_mode = True


# Workout Plan Schemas
class WorkoutPlanBase(BaseModel):
    name: str
    description: Optional[str] = None


class WorkoutPlanCreate(WorkoutPlanBase):
    pass


class WorkoutPlanResponse(WorkoutPlanBase):
    id: int
    created_at: Optional[datetime]
    user_id: int

    class Config:
        orm_mode = True


# Exercise Schemas
class ExerciseBase(BaseModel):
    name: str
    instructions: Optional[str] = None
    image_url: Optional[str] = None
    difficulty: Optional[int] = Field(ge=1, le=5, description="Difficulty must be between 1 (easy) and 5 (hard)")


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseResponse(ExerciseBase):
    id: int

    class Config:
        orm_mode = True


# Workout Exercise Schemas
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


# Progress Log Schemas
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
    workout_plan_id: Optional[int]

    class Config:
        orm_mode = True