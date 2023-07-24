from fastapi import APIRouter

from db import orders, database
from models import Order, OrderIn

router = APIRouter()


# _____________________ORDERS____________________________


@router.get("/orders", response_model=list[Order])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.post("/orders", response_model=Order)
async def create_orders(order: OrderIn):
    query = orders.insert().values(
        order_date=order.order_date,
        status=order.status,
        user_id=order.user_id,
        goods_id=order.goods_id
    )
    last_record_id = await database.execute(query)
    return {**orders.dict(), "id": last_record_id}


@router.get("/orders/{orders_id}", response_model=Order)
async def read_order(orders_id: int):
    query = orders.select().where(orders.c.id == orders_id)
    return await database.fetch_one(query)


@router.put("/orders/{orders_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id ==
                                  order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


@router.delete("/orders/{goods_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'goods deleted'}