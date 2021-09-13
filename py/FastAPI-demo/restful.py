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


@app.get('/item/{id}')
async def get_item(id: int):
    return {"id": id}


@app.get('/items')
async def get_items(limit: Optional[int] = None, offset: Optional[int] = None):
    return {"limit": limit, "offset": offset}


class Item(BaseModel):
    title: str
    content: str
    user: int


@app.post('/item')
async def create_item(item: Item):
    return item

if __name__ == '__main__':
    import os
    os.system('')
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
