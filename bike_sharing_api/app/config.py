import os

class Config:
    MODEL_PATH = os.getenv('MODEL_PATH', 'bike_sharing_model-0.0.1-py3-none-any.whl')
