from fastapi import APIRouter

router = APIRouter(tags=["Threats"])

@router.get("/threats")
def threats():
    return {
        "active_threats": 2,
        "risk_level": "medium",
        "status": "monitoring"
    }