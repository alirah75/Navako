import asyncio
from fastapi import APIRouter, Body, status
from schemas.predict import PredictSentence
from model.Model import load_model, analysis_sentence


router = APIRouter()
model = load_model()


@router.post('/', response_model=list, status_code=status.HTTP_201_CREATED)
async def predict(sentence: PredictSentence = Body(...)):
    task = asyncio.create_task(analysis_sentence(model, sentence.sentence))
    return await task
