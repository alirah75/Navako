from fastapi import APIRouter, status

router = APIRouter()


@router.get('/health', response_model=dict, status_code=status.HTTP_200_OK)
def health():
    return {"status": "Ok"}