from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models import User
from models import WorkoutPlan


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register", response_class=HTMLResponse)
async def register_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: AsyncSession = Depends(get_db),
):
    # Check if the email already exists
    result = await db.execute(select(User).where(User.email == email))
    existing_user = result.scalars().first()
    if existing_user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Email already registered."})

    # Create a new user with plain-text password (not secure)
    new_user = User(username=username, email=email, password=password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return templates.TemplateResponse("login.html", {"request": request, "message": "Registration successful!"})


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login", response_class=HTMLResponse)
async def login_user(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: AsyncSession = Depends(get_db),
):
    # Find user by email
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()

    # Validate plain-text password (not secure)
    if not user or user.password != password:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()  # Example: Fetching all users
    return templates.TemplateResponse("dashboard.html", {"request": request, "users": users})


@app.get("/workout", response_class=HTMLResponse)
async def workout_page(request: Request, db: AsyncSession = Depends(get_db)):
    user_id = 1  # Replace this with actual user logic
    result = await db.execute(select(WorkoutPlan).where(WorkoutPlan.user_id == user_id))
    workout_plans = result.scalars().all()

    return templates.TemplateResponse("workout.html", {"request": request, "workout_plans": workout_plans})

@app.post("/workout", response_class=HTMLResponse)
async def add_workout(
    request: Request,
    name: str = Form(...),
    description: str = Form(...),
    user_id: int = 1,  # Replace this with actual user session ID logic
    db: AsyncSession = Depends(get_db),
):
    # Insert the workout plan into the database
    from models import WorkoutPlan

    new_workout = WorkoutPlan(
        user_id=user_id,  # Link the workout plan to the logged-in user
        name=name,
        description=description,
    )
    db.add(new_workout)
    await db.commit()
    await db.refresh(new_workout)

    # Fetch all workout plans to render updated page
    result = await db.execute(select(WorkoutPlan).where(WorkoutPlan.user_id == user_id))
    workout_plans = result.scalars().all()

    return templates.TemplateResponse(
        "workout.html", {"request": request, "workout_plans": workout_plans, "message": "Workout added successfully!"}
    )

@app.get("/exercises", response_class=HTMLResponse)
async def exercises(request: Request):
    return templates.TemplateResponse("exercises.html", {"request": request})


@app.post("/forgot_password", response_class=HTMLResponse)
async def forgot_password(request: Request, email: str = Form(...), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()

    if user:
        message = "Password recovery email has been sent."  # Logic for email sending is not implemented here
    else:
        message = "Email not found."

    return templates.TemplateResponse("forgot_password.html", {"request": request, "message": message})
