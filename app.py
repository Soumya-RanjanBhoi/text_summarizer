from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors  import CORSMiddleware
from textSummarizer.pipeline.prediction import PredictionPipelines
from enum import Enum
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


@app.post("/")
async def starting():
    return {"Summarizartion + translation"}   

@app.post("/predict")
async def predict(text: str, length_category: LengthCategory):
    try:
        if length_category == LengthCategory.short:
            length = 100
        elif length_category == LengthCategory.medium:
            length = 180
        else:
            length = 300
        
        text = "summarize: " + text

        ans = PredictionPipelines().summarize(text, length)
        return {"summary": ans,}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/translate")
async def translate(text:str):
    try:
        trans_text=PredictionPipelines().translate(text)
        return {"translated_text":trans_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



