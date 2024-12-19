from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from sqlalchemy.orm import Session

from database import Base, engine, get_db  # Import database logic
import models  # Import models for table creation

# Initialize FastAPI app
app = FastAPI()

# Create database tables (if not already created)
Base.metadata.create_all(bind=engine)

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes with database session dependency
@app.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Session = Depends(get_db)):
    # Example query (just for demonstration, remove if not needed)
    users = db.query(models.User).all()
    return templates.TemplateResponse("home.html", {"request": request, "users": users})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    # Example query (fetch data for dashboard, if needed)
    plans = db.query(models.WorkoutPlan).all()
    return templates.TemplateResponse("dashboard.html", {"request": request, "plans": plans})

@app.get("/workout", response_class=HTMLResponse)
async def workout(request: Request, db: Session = Depends(get_db)):
    # Example query for workout plans
    workouts = db.query(models.WorkoutPlan).all()
    return templates.TemplateResponse("workout.html", {"request": request, "workouts": workouts})

@app.get("/exercises", response_class=HTMLResponse)
async def exercises(request: Request, db: Session = Depends(get_db)):
    # Example query for exercises
    exercises = db.query(models.Exercise).all()
    return templates.TemplateResponse("exercises.html", {"request": request, "exercises": exercises})

@app.get("/forgot_password", response_class=HTMLResponse)
async def forgot_password(request: Request):
    return templates.TemplateResponse("forgot_password.html", {"request": request})




# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from starlette.responses import HTMLResponse
# # from crud import *
# # from database import get_DB
# app = FastAPI()
#
# templates = Jinja2Templates(directory="templates")
# app.mount("/static",StaticFiles(directory="static"),name="static")
#
# @app.get("/", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request})
#
# @app.get("/about", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("about.html", {"request": request})
#
# @app.get("/register", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("register.html", {"request": request})
#
# @app.get("/login", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})
#
# @app.get("/dashboard", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("dashboard.html", {"request": request})
#
# @app.get("/workout", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("workout.html", {"request": request})
#
# @app.get("/exercises", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("exercises.html", {"request": request})
#
# @app.get("/forgot_password", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("forgot_password.html", {"request": request})







# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from starlette.responses import HTMLResponse
#
# app = FastAPI()
#
# templates = Jinja2Templates(directory="templates")
#
# @app.get("/", response_class=HTMLResponse)
# async def index():
#     return templates.TemplateResponse("home.html", {"request": request})