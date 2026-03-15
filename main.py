from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from engine import EmpathyEngine
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
engine = EmpathyEngine()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "audio_url": None, "emotion": None, "intensity": None})

@app.post("/generate", response_class=HTMLResponse)
async def generate_speech(request: Request, text: str = Form(...)):
    audio_url, emotion, intensity = engine.generate_audio(text)
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "audio_url": audio_url, 
        "emotion": emotion, 
        "intensity": round(intensity, 2),
        "input_text": text
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
