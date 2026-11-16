from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from ..config import settings
from ..database import get_db
from ..models.category import Category
from ..models.service import Service
from ..models.user import User
from ..models.order import Order
from ..models.transaction import Transaction
from ..security import verify_api_key

router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"]
)


@router.get("/dashboard", dependencies=[Depends(verify_api_key)])
def admin_dashboard(db: Session = Depends(get_db)):
    return {
        "total_users": db.query(User).count(),
        "total_categories": db.query(Category).count(),
        "total_services": db.query(Service).count(),
        "total_orders": db.query(Order).count(),
        "total_transactions": db.query(Transaction).count()
    }


@router.get("/users", dependencies=[Depends(verify_api_key)])
def admin_users(db: Session = Depends(get_db)):
    users = db.query(User).order_by(User.id.desc()).limit(100).all()

    return [
        {
            "id": user.id,
            "telegram_id": user.telegram_id,
            "username": user.username,
            "full_name": user.full_name,
            "balance": user.balance,
            "is_active": user.is_active
        }
        for user in users
    ]
