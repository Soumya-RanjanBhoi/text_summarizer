from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from textSummarizer.pipeline.prediction import PredictionPipelines
from enum import Enum
import os
import uvicorn

app = FastAPI()

class LengthCategory(str, Enum):
    short = "short"
    medium = "medium"
    long = "long"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline_instance = PredictionPipelines()

@app.get("/healthz")
async def health_check():
    return {"status": "healthy"}

@app.post("/")
async def starting():
    return {"message": "Summarization + Translation API is running"}

@app.post("/predict")
async def predict(text: str, length_category: LengthCategory):
    try:
        if length_category == LengthCategory.short:
            length = 100
        elif length_category == LengthCategory.medium:
            length = 200
        else:
            length = 300

        text = "summarize: " + text
        ans = pipeline_instance.summarize(text, length)
        return {"summary": ans}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/translate")
async def translate(text: str):
    try:
        trans_text = pipeline_instance.translate(text)
        return {"translated_text": trans_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  
    uvicorn.run(app, host="0.0.0.0", port=port)

