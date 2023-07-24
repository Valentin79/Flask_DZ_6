from fastapi import APIRouter

from db import goods, database
from models import Goods, GoodsIn

router = APIRouter()


# _____________________GOODS____________________________


@router.get("/goods", response_model=list[Goods], tags=["goods"])
async def get_googs():
    query = goods.select()
    return await database.fetch_all(query)


@router.post("/goods", response_model=Goods)
async def create_goods(item: GoodsIn):
    query = goods.insert().values(
        title=item.title,
        description=item.description,
        price=item.price
    )
    last_record_id = await database.execute(query)
    return {**goods.dict(), "id": last_record_id}


@router.get("/goods/{goods_id}", response_model=Goods)
async def read_goods(goods_id: int):
    query = goods.select().where(goods.c.id == goods_id)
    return await database.fetch_one(query)


@router.put("/goods/{goods_id}", response_model=Goods)
async def update_goods(goods_id: int, new_item: GoodsIn):
    query = goods.update().where(goods.c.id ==
                                 goods_id).values(**new_item.dict())
    await database.execute(query)
    return {**new_item.dict(), "id": goods_id}


@router.delete("/goods/{goods_id}")
async def delete_goods(goods_id: int):
    query = goods.delete().where(goods.c.id == goods_id)
    await database.execute(query)
    return {'message': 'goods deleted'}