from pydantic import BaseModel, ConfigDict, Field


class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: str | None = None


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str | None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class ServiceCreate(BaseModel):
    category_id: int
    name: str = Field(min_length=2, max_length=200)
    description: str | None = None
    price: float = Field(ge=0)


class ServiceResponse(BaseModel):
    id: int
    category_id: int
    name: str
    description: str | None
    price: float
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class OrderCreate(BaseModel):
    service_id: int
    target_url: str = Field(min_length=1, max_length=1000)
    quantity: int = Field(gt=0)


class OrderResponse(BaseModel):
    id: int
    user_id: int
    service_id: int
    target_url: str
    quantity: int
    charge: float
    status: str

    model_config = ConfigDict(from_attributes=True)
