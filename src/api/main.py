from fastapi import FastAPI

from src.api.routes.chat import router as chat_router
from src.api.routes.forecast import router as forecast_router
from src.api.routes.analytics import router as analytics_router
from src.api.routes.report import router as report_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AI Demand Intelligence Platform",
    description="AI-powered Demand Intelligence Backend API",
    version="10.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:4173",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:4173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "AI Demand Intelligence Platform",
    }


app.include_router(chat_router)
app.include_router(forecast_router)
app.include_router(analytics_router)
app.include_router(report_router)