from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/workout", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("workout.html", {"request": request})

@app.get("/exercises", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("exercises.html", {"request": request})

@app.get("/forgot_password", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("forgot_password.html", {"request": request})







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