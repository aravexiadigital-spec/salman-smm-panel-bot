from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.service import Service
from ..models.category import Category
from ..schemas import ServiceResponse

router = APIRouter(
    prefix="/api/services",
    tags=["Services"]
)


@router.get("/", response_model=list[ServiceResponse])
def get_services(
    category_id: int | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Service).filter(
        Service.is_active.is_(True)
    )

    if category_id is not None:
        query = query.filter(
            Service.category_id == category_id
        )

    return query.order_by(Service.id.desc()).all()


@router.get("/{service_id}", response_model=ServiceResponse)
def get_service(
    service_id: int,
    db: Session = Depends(get_db)
):
    service = db.query(Service).filter(
        Service.id == service_id,
        Service.is_active.is_(True)
    ).first()

    if service is None:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return service
