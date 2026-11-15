from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import settings


class Base(DeclarativeBase):
    pass


engine = None
SessionLocal = None

if settings.DATABASE_URL:
    database_url = settings.DATABASE_URL

    if database_url.startswith("postgres://"):
        database_url = database_url.replace(
            "postgres://",
            "postgresql://",
            1
        )

    engine = create_engine(
        database_url,
        pool_pre_ping=True
    )

    SessionLocal = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False
    )


def get_db():
    if SessionLocal is None:
        raise HTTPException(
            status_code=503,
            detail="Database is not configured"
        )

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
