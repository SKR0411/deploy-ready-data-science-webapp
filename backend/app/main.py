from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from . import api
from pathlib import Path

app = FastAPI(title="Data Science Web App")
app.include_router(api.router, prefix="/api")

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Mount static if needed (for CSS/JS)
app.mount("/static", StaticFiles(directory=str(Path(__file__).resolve().parent / "static")), name="static")

# For container entrypoint: uvicorn app.main:app --host 0.0.0.0 --port 8000