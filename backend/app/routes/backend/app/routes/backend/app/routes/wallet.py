from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.wallet import Wallet
from ..models.transaction import Transaction
from ..security import verify_api_key

router = APIRouter(
    prefix="/api/wallet",
    tags=["Wallet"]
)


@router.get(
    "/",
    dependencies=[Depends(verify_api_key)]
)
def get_wallets(
    db: Session = Depends(get_db)
):
    wallets = (
        db.query(Wallet)
        .order_by(Wallet.id.desc())
        .limit(100)
        .all()
    )

    return [
        {
            "id": wallet.id,
            "user_id": wallet.user_id,
            "balance": wallet.balance,
            "updated_at": wallet.updated_at
        }
        for wallet in wallets
    ]


@router.get(
    "/transactions",
    dependencies=[Depends(verify_api_key)]
)
def get_transactions(
    db: Session = Depends(get_db)
):
    transactions = (
        db.query(Transaction)
        .order_by(Transaction.id.desc())
        .limit(100)
        .all()
    )

    return [
        {
            "id": item.id,
            "user_id": item.user_id,
            "amount": item.amount,
            "type": item.transaction_type,
            "status": item.status,
            "reference": item.reference,
            "created_at": item.created_at
        }
        for item in transactions
    ]
