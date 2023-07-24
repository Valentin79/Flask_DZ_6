import sqlalchemy
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, \
    Text, Float, DATE, ForeignKey, DateTime, Date
import databases as databases

from settings import settings

db = settings.DATABASE_URL
database = databases.Database(db)
metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("email", String(50)),
    Column("password", String(120)),
)

goods = sqlalchemy.Table(
    "goods",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", Text(200)),
    Column("price", Float)
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_date", Date),
    Column('status', String(20)),
    Column("user_id", ForeignKey("users.id"), nullable=False),
    Column("goods_id", ForeignKey("goods.id"), nullable=False)
)

engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)