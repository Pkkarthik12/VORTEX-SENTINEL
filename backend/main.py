from fastapi import FastAPI
from routers.telemetry import router as telemetry_router
from routers.health import router as health_router
from routers.threats import router as threats_router

app = FastAPI(title="VORTEX-SENTINEL")

app.include_router(telemetry_router)
app.include_router(health_router)
app.include_router(threats_router)

@app.get("/")
def root():
    return {
        "platform": "VORTEX-SENTINEL",
        "status": "running",
        "mode": "AI Infrastructure Intelligence"
    }