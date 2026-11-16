from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import categories, services, orders, wallet, admin, deposits

app = FastAPI(
    title="SALMAN SMM PANEL API",
    description="Telegram SMM Panel Management API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type", "X-API-Key"],
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
        "service": "SALMAN SMM PANEL API"
    }


app.include_router(categories.router)
app.include_router(services.router)
app.include_router(orders.router)
app.include_router(wallet.router)
app.include_router(admin.router)
app.include_router(deposits.router)
