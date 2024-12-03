import asyncio
from transformers import pipeline


def load_model():
    pipe = pipeline("text-classification", model="HooshvareLab/bert-fa-base-uncased-sentiment-digikala")
    return pipe


async def analysis_sentence(pipe, sentence):
    loop = asyncio.get_event_loop()
    results = await loop.run_in_executor(None, pipe, sentence)
    return results
