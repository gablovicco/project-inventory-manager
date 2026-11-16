from contextlib import asynccontextmanager
from typing import Annotated
from sqlmodel import Session, select

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from fastapi import Depends, FastAPI
from sqlmodel import Session

from app.database import create_db_and_tables, get_session
from app.models import Product, ProductCreate, ProductPublic
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import create_db_and_tables
from app.models import Product


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/health")
def health_check():
    return {"status": "ok"}
@app.get("/", response_class=FileResponse)
def read_index():
    return "app/static/index.html"

@app.post("/products", response_model=ProductPublic, status_code=201)
def create_product(
    product: ProductCreate,
    session: Annotated[Session, Depends(get_session)],
):
    db_product = Product.model_validate(product)

    session.add(db_product)
    session.commit()
    session.refresh(db_product)

    return db_product

@app.get("/products", response_model=list[ProductPublic])
def read_products(
    session: Annotated[Session, Depends(get_session)],
):
    products = session.exec(select(Product)).all()
    return products