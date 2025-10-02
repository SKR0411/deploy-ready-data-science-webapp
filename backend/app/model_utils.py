import joblib
from pathlib import Path
from typing import List

MODEL_PATH = Path(__file__).resolve().parent.parent / "model.joblib"

_model = None

def load_model():
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Run training.")
        _model = joblib.load(MODEL_PATH)
    return _model


def predict(features: List[float]):
    model = load_model()
    import numpy as np
    X = np.array(features).reshape(1, -1)
    pred = int(model.predict(X)[0])
    probs = model.predict_proba(X)[0].tolist() if hasattr(model, 'predict_proba') else []
    return pred, probs