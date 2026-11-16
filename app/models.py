from pydantic import field_validator
from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    name: str
    current_quantity: int = Field(default=0, ge=0)
    minimum_stock_level: int = Field(default=0, ge=0)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Product name cannot be empty")

        return value


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    pass


class ProductPublic(ProductBase):
    id: int