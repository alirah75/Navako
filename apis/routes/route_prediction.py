import asyncio
from fastapi import APIRouter, Body, status, HTTPException

from apis.routes import model
from schemas.predict import PredictSentence
from model.Model import analysis_sentence

router = APIRouter()


@router.post('/',
             response_model=list,
             status_code=status.HTTP_201_CREATED,
             summary="Predict emotion",
             description="Send a text and get the predicted emotion.")
async def predict(sentence: PredictSentence = Body(...)):
    if model is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Model is not available.")
    try:
        task = asyncio.create_task(analysis_sentence(model, sentence.sentence))
        return await task
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error during prediction: {e}")
