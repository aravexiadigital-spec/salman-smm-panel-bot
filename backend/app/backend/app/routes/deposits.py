from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.deposit import Deposit
from ..security import verify_api_key

router = APIRouter(
    prefix="/api/deposits",
    tags=["Deposits"]
)


@router.get("/", dependencies=[Depends(verify_api_key)])
def get_deposits(db: Session = Depends(get_db)):
    deposits = (
        db.query(Deposit)
        .order_by(Deposit.id.desc())
        .limit(100)
        .all()
    )

    return [
        {
            "id": item.id,
            "user_id": item.user_id,
            "amount": item.amount,
            "payment_method": item.payment_method,
            "transaction_reference": item.transaction_reference,
            "status": item.status,
            "created_at": item.created_at
        }
        for item in deposits
    ]
