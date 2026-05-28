from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health")
def health():
    return {
        "backend": "healthy",
        "database": "connected",
        "ai_engine": "active"
    }