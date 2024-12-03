from pydantic import BaseModel, Field


class PredictSentence(BaseModel):
    sentence: str = Field(..., max_length=50)
