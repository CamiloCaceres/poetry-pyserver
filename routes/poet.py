from fastapi import APIRouter

from models.poet import Poet
from config.db import db
from schemas.serlialize import serializeDict, serializeList
from bson import ObjectId

poet = APIRouter(
    prefix="/api/v1/poets",
    tags=["poets"],
    responses={404: {"description": "Not found"}},
)

@poet.get('/')
async def find_all_poets():
    return serializeList(db.poet.find())

@poet.get('/{id}')
async def find_one_poets(id):
    return serializeDict(db.poet.find_one({"_id":ObjectId(id)}))

@poet.post('/')
async def create_poet(poet: Poet):
    db.poet.insert_one(dict(poet))
    return serializeList(db.poet.find())

@poet.put('/{id}')
async def update_poet(id, poet: Poet):
    db.poet.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(poet)
    })
    return serializeDict(db.poet.find_one({"_id":ObjectId(id)}))

@poet.delete('/{id}')
async def delete_poet(id, poet: Poet):
    return serializeDict(db.poet.find_one_and_delete({"_id":ObjectId(id)}))