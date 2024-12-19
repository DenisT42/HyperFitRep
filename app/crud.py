from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from models import User, WorkoutPlan, Exercise, WorkoutExercise, ProgressLog
from schemas import UserCreate, WorkoutPlanCreate, ExerciseCreate, ProgressLogCreate


# User CRUD Operations
async def create_user(db: AsyncSession, user_data: UserCreate):
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password,  # Hash password before storing in production
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()


# Workout Plan CRUD Operations
async def create_workout_plan(db: AsyncSession, plan_data: WorkoutPlanCreate, user_id: int):
    new_plan = WorkoutPlan(
        user_id=user_id,
        name=plan_data.name,
        description=plan_data.description,
    )
    db.add(new_plan)
    await db.commit()
    await db.refresh(new_plan)
    return new_plan


async def get_workout_plan_by_id(db: AsyncSession, plan_id: int):
    result = await db.execute(select(WorkoutPlan).where(WorkoutPlan.id == plan_id))
    return result.scalars().first()


async def get_workout_plans(db: AsyncSession, user_id: int):
    result = await db.execute(select(WorkoutPlan).where(WorkoutPlan.user_id == user_id))
    return result.scalars().all()


async def delete_workout_plan(db: AsyncSession, plan_id: int):
    plan = await get_workout_plan_by_id(db, plan_id)
    if plan:
        await db.delete(plan)
        await db.commit()
        return True
    return False


# Exercise CRUD Operations
async def create_exercise(db: AsyncSession, exercise_data: ExerciseCreate):
    new_exercise = Exercise(
        name=exercise_data.name,
        instructions=exercise_data.instructions,
        image_url=exercise_data.image_url,
        difficulty=exercise_data.difficulty,
    )
    db.add(new_exercise)
    await db.commit()
    await db.refresh(new_exercise)
    return new_exercise


async def get_exercises(db: AsyncSession):
    result = await db.execute(select(Exercise))
    return result.scalars().all()


async def get_exercise_by_id(db: AsyncSession, exercise_id: int):
    result = await db.execute(select(Exercise).where(Exercise.id == exercise_id))
    return result.scalars().first()


# Progress Log CRUD Operations
async def create_progress_log(db: AsyncSession, log_data: ProgressLogCreate, user_id: int):
    new_log = ProgressLog(
        user_id=user_id,
        date=log_data.date,
        workout_plan_id=log_data.workout_plan_id,
        total_calories=log_data.total_calories,
        total_duration=log_data.total_duration,
        avg_heart_rate=log_data.avg_heart_rate,
    )
    db.add(new_log)
    await db.commit()
    await db.refresh(new_log)
    return new_log


async def get_progress_logs(db: AsyncSession, user_id: int):
    result = await db.execute(
        select(ProgressLog)
        .where(ProgressLog.user_id == user_id)
        .options(joinedload(ProgressLog.workout_plan))
    )
    return result.scalars().all()