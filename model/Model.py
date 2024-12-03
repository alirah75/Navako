import asyncio
from transformers import pipeline


def load_model():
    try:
        model = pipeline("text-classification", model="HooshvareLab/bert-fa-base-uncased-sentiment-digikala")
        return model
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")


async def analysis_sentence(model, sentence):
    loop = asyncio.get_event_loop()
    try:
        results = await loop.run_in_executor(None, model, sentence)
        return results
    except Exception as e:
        raise RuntimeError(f"Error during sentence analysis: {e}")
