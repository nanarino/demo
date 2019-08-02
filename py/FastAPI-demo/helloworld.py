from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main():
    return {"msg": "helloworld"}


@app.get('/{item}/')
async def get_item(item):
    return {"msg": item}

if __name__ == '__main__':
    import os
    os.system('')
    import uvicorn
    uvicorn.run(app='helloworld:app', host="0.0.0.0",
                port=80, reload=True, debug=True)
