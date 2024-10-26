
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from datetime import datetime
import pytz
import numpy as np
import pandas as pd

from taxifare.interface.main import load_model, preprocess_features

app = FastAPI()

# # Load the model into memory on startup
# @app.on_event("startup")
# async def load_model_into_memory():
#     app.state.model = load_model()
#     if app.state.model is None:
#         raise HTTPException(status_code=500, detail="Model could not be loaded")

# # Define a Pydantic model for the query parameters
# class PredictRequest(BaseModel):
#     pickup_datetime: datetime
#     pickup_longitude: float
#     pickup_latitude: float
#     dropoff_longitude: float
#     dropoff_latitude: float
#     passenger_count: int

# @app.get("/predict")
# async def predict(request: PredictRequest):
#     # Convert pickup_datetime to the correct timezone
#     eastern = pytz.timezone('US/Eastern')
#     pickup_datetime = request.pickup_datetime.astimezone(eastern)

#     # Build X_pred
#     X_pred = pd.DataFrame(dict(
#         pickup_datetime=[pickup_datetime],
#         pickup_longitude=[request.pickup_longitude],
#         pickup_latitude=[request.pickup_latitude],
#         dropoff_longitude=[request.dropoff_longitude],
#         dropoff_latitude=[request.dropoff_latitude],
#         passenger_count=[request.passenger_count],
#     ))

#     # Preprocess the features
#     X_processed = preprocess_features(X_pred)

#     try:
#         # Make prediction using the model loaded into memory
#         fare = app.state.model.predict(X_processed)
#         return {'fare': fare.tolist()[0]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Root endpoint
@app.get("/")
async def root():
    return {'greeting': 'Hello'}
