from pydantic import BaseModel, Field, EmailStr


from settings import settings
from datetime import date, datetime


class User(BaseModel):
    __tablename__ = "users"
    id: int
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: str = Field(..., max_length=50)
    password: str = Field(..., max_length=120)


class UserIn(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: str = Field(..., max_length=50)
    password: str = Field(...,  max_length=120)


class Goods(BaseModel):
    __tablename__ = "goods"
    id: int
    title: str = Field(..., max_length=50)
    description: str = Field(..., max_length=200)
    price: float = Field(..., le=100000)


class GoodsIn(BaseModel):
    title: str = Field(..., max_length=50)
    description: str = Field(..., max_length=200)
    price: float = Field(..., le=100000)


class Order(BaseModel):
    __tablename__ = "orders"
    id: int
    # order_date: date = Field(default=datetime.now(), format="%d-%m-%Y")
    order_date: date = Field(format="%d-%m-%Y")
    status: str = Field(default='in_progress')
    user_id: int
    goods_id: int


class OrderIn(BaseModel):
    # order_date: date = Field(default=datetime.now(), format="%d-%m-%Y")
    order_date: date = Field(format="%d-%m-%Y")
    status: str = Field(default='in_progress')
    user_id: int
    goods_id: int
