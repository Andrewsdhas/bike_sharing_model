from pydantic import BaseModel

class PredictRequest(BaseModel):
    feature1: float
    feature2: float
    # Add all required features
