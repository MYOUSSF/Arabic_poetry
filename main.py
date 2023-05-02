import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.model.model import classify
from fastapi import Form

templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

app = FastAPI()
templates = Jinja2Templates(directory=templates_dir)


#
#
class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, text: str = Form(...)):
    meter = classify(text)[0]
    return templates.TemplateResponse("index.html", {"request": request, "output": meter})
