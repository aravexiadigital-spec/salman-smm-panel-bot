from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SALMAN SMM PANEL API",
    description="Telegram SMM Panel Management API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production এ নির্দিষ্ট domain দেবে
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)


@app.get("/")
async def home():
    return {
        "success": True,
        "project": "SALMAN SMM PANEL",
        "message": "Backend is running"
    }


@app.get("/api/health")
async def health():
    return {
        "status": "healthy",
        "service": "SALMAN SMM PANEL API",
        "version": "1.0.0"
    }


@app.get("/api")
async def api_info():
    return {
        "name": "SALMAN SMM PANEL API",
        "status": "active",
        "docs": "/docs"
  }
