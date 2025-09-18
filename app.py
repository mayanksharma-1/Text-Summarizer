import uvicorn
import sys
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel # Import BaseModel for input validation
from text_summarizer.pipeline.prediction import PredictionPipeline

# Define a Pydantic model for the request body
class TextIn(BaseModel):
    text: str

app = FastAPI()

# Initialize the Jinja2Templates with the templates directory
templates = Jinja2Templates(directory="templates")

# Initialize the model object once for efficiency
model_predictor = PredictionPipeline()

@app.get("/", tags=["UI"], response_class=HTMLResponse)
async def home(request: Request):
    """Serve the HTML front-end."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/train", tags=["training"])
async def training():
    """Triggers the model training pipeline."""
    try:
        os.system("python main.py")
        return {"message": "Training successful!"}
    except Exception as e:
        return {"message": f"Error Occurred! {e}"}

@app.post("/predict_web", tags=["prediction"])
async def predict_route(text_in: TextIn):
    """Receives text from the web form and returns a summary."""
    try:
        summary = model_predictor.predict(text_in.text)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)