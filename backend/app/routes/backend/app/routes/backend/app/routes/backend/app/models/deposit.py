from datetime import datetime, timezone

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class Deposit(Base):
    __tablename__ = "deposits"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    payment_method: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    transaction_reference: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
