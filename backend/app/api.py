from fastapi import APIRouter, HTTPException
from .schemas import PredictRequest, PredictResponse
from .model_utils import predict

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
async def predict_endpoint(req: PredictRequest):
    try:
        pred, probs = predict(req.features)
        return {"prediction": pred, "probabilities": probs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))