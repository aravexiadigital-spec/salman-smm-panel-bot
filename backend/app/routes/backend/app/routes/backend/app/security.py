import hmac

from fastapi import Header, HTTPException, status

from .config import settings


def verify_api_key(
    x_api_key: str = Header(default="")
):
    configured_key = settings.API_SECRET

    if not configured_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="API security is not configured"
        )

    if not hmac.compare_digest(
        x_api_key,
        configured_key
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )

    return True
