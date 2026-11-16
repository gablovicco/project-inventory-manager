import pytest
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from app.database import get_session
from app.main import app


test_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


def get_test_session():
    with Session(test_engine) as session:
        yield session


app.dependency_overrides[get_session] = get_test_session

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_database():
    SQLModel.metadata.drop_all(test_engine)
    SQLModel.metadata.create_all(test_engine)
    yield


def test_create_product():
    response = client.post(
        "/products",
        json={
            "name": "Keyboard",
            "current_quantity": 10,
            "minimum_stock_level": 3,
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Keyboard"
    assert data["current_quantity"] == 10
    assert data["minimum_stock_level"] == 3
    assert isinstance(data["id"], int)


def test_create_product_rejects_negative_quantity():
    response = client.post(
        "/products",
        json={
            "name": "Mouse",
            "current_quantity": -5,
            "minimum_stock_level": 2,
        },
    )

def test_create_product_rejects_negative_minimum_stock_level():
    response = client.post(
        "/products",
        json={
            "name": "Mouse",
            "current_quantity": 5,
            "minimum_stock_level": -1,
        },
    )

    assert response.status_code == 422



def test_create_product_rejects_empty_name():
    response = client.post(
        "/products",
        json={
            "name": "   ",
            "current_quantity": 5,
            "minimum_stock_level": 2,
        },
    )

    assert response.status_code == 422


def test_create_product_trims_name():
    response = client.post(
        "/products",
        json={
            "name": "  Mouse  ",
            "current_quantity": 5,
            "minimum_stock_level": 2,
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Mouse"

def test_read_products():
    client.post(
        "/products",
        json={
            "name": "Keyboard",
            "current_quantity": 10,
            "minimum_stock_level": 3,
        },
    )

    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Keyboard"
    assert data[0]["current_quantity"] == 10
    assert data[0]["minimum_stock_level"] == 3

def test_home_page():
    response = client.get("/")

    assert response.status_code == 200
    assert "Inventory Manager" in response.text
    assert "Add Product" in response.text