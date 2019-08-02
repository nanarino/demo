from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    title: str = '无题'
    content: str


@app.get('/item/{id}')
async def get_item(id: int):
    return {"id": id}


@app.get('/items')
async def get_items(limit: Optional[int] = None, offset: Optional[int] = None):
    return {"limit": limit, "offset": offset}


@app.post('/item')
async def create_item(item: Item):
    return item


@app.put('/item/{id}')
async def update_item(id: int, item: Item):
    return {"id": id, "item": item}


@app.delete('/item/{id}')
async def delete_item(id: int, item: Item):
    return {"id": id, "item": item}

if __name__ == '__main__':
    import os
    os.system('')
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
