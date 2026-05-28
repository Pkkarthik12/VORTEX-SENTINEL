from fastapi import APIRouter
import random

router = APIRouter(prefix="/telemetry", tags=["Telemetry"])

@router.get("/live")
def live():
    return {
        "temperature": round(random.uniform(25, 75), 2),
        "voltage": round(random.uniform(210, 240), 2),
        "anomaly_score": round(random.uniform(0, 1), 3)
    }