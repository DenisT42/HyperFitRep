from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from database import get_db, Base, engine
import models
import crud

# Initialize FastAPI application
app = FastAPI()

# Initialize templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create database tables at startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Error handling for 404
@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    raise exc


# Route: Home Page
@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# Route: About Page
@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


# Route: Register
@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


# Route: Login
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# Route: Dashboard (requires database access)
@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, db: AsyncSession = Depends(get_db)):
    user_data = await crud.get_all_users(db)  # Example query for all users
    return templates.TemplateResponse("dashboard.html", {"request": request, "users": user_data})


# Route: Workout Plans
@app.get("/workout", response_class=HTMLResponse)
async def workout_page(request: Request, db: AsyncSession = Depends(get_db)):
    workout_plans = await crud.get_workout_plans(db)  # Fetch all workout plans
    return templates.TemplateResponse("workout.html", {"request": request, "workout_plans": workout_plans})


# Route: Exercises
@app.get("/exercises", response_class=HTMLResponse)
async def exercises_page(request: Request, db: AsyncSession = Depends(get_db)):
    exercises = await crud.get_exercises(db)  # Fetch exercises
    return templates.TemplateResponse("exercises.html", {"request": request, "exercises": exercises})


# Route: Forgot Password
@app.get("/forgot_password", response_class=HTMLResponse)
async def forgot_password_page(request: Request):
    return templates.TemplateResponse("forgot_password.html", {"request": request})


# Example Protected Route (future authentication setup)
@app.get("/protected", response_class=HTMLResponse)
async def protected_page(request: Request):
    # This can later be integrated with JWT or session-based authentication
    raise HTTPException(status_code=401, detail="Unauthorized access")