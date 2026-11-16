from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.order import Order
from ..security import verify_api_key

router = APIRouter(
    prefix="/api/orders",
    tags=["Orders"]
)


@router.get(
    "/",
    dependencies=[Depends(verify_api_key)]
)
def get_orders(
    limit: int = 50,
    db: Session = Depends(get_db)
):
    if limit < 1 or limit > 100:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 100"
        )

    orders = (
        db.query(Order)
        .order_by(Order.id.desc())
        .limit(limit)
        .all()
    )

    return [
        {
            "id": order.id,
            "user_id": order.user_id,
            "service_id": order.service_id,
            "target_url": order.target_url,
            "quantity": order.quantity,
            "charge": order.charge,
            "status": order.status,
            "created_at": order.created_at
        }
        for order in orders
    ]
