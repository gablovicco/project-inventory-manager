from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    current_quantity: int = 0
    minimum_stock_level: int = 0