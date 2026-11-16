from .database import Base, engine
from . import models


def initialize_database():
    if engine is None:
        raise RuntimeError("DATABASE_URL is not configured")

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    initialize_database()
    print("Database tables created successfully!")
