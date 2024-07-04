from pydantic import BaseModel

class HealthResponse(BaseModel):
    name: str
    version: str
    model_version: str
