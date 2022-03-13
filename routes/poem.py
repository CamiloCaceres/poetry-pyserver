from fastapi import APIRouter

from models.poem import Poem
from config.db import db
from schemas.serlialize import serializeDict, serializeList
from bson import ObjectId

poem = APIRouter(
    prefix="/api/v1/poems",
    tags=["poems"],
    responses={404: {"description": "Not found"}},
)

@poem.get('/')
async def find_all_poems():
    return serializeList(db.poem.find())

@poem.get('/{id}')
async def find_one_poems(id):
    return serializeDict(db.poem.find_one({"_id":ObjectId(id)}))

@poem.post('/')
async def create_poem(poem: Poem):
    db.poem.insert_one(dict(poem))
    return serializeList(db.poem.find())

@poem.put('/{id}')
async def update_poem(id, poem: Poem):
    db.poem.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(poem)
    })
    return serializeDict(db.poem.find_one({"_id":ObjectId(id)}))

@poem.delete('/{id}')
async def delete_poem(id, poem: Poem):
    return serializeDict(db.poem.find_one_and_delete({"_id":ObjectId(id)}))