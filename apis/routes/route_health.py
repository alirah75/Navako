from fastapi import APIRouter, status, HTTPException
from apis.routes import model

router = APIRouter()


@router.get('/',
            response_model=dict,
            status_code=status.HTTP_200_OK,
            summary="Check API health",
            description="Check if the API service is running")
def health():
    try:
        test_sentence = "این یک جمله آزمایشی است."
        prediction = model(test_sentence)
        return {"status": "Ok", "details": "Model is running ...", "prediction_sample": prediction}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Model error: {str(e)}")
