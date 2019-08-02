from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_ip(req: Request):
    forwarded = req.headers.get("X-Forwarded-For")
    if forwarded:
        ip = forwarded.split(",")[0]
    else:
        ip = req.client.host
    return ip

@app.post("/submit/")
async def post_form(req: Request, ip = Depends(get_ip)):
    print(ip)
    form_data = await req.form()
    return dict(form_data.items())

if __name__ == '__main__':
    import os
    os.system('')
    import uvicorn
    uvicorn.run(app="app:app", host="0.0.0.0", port=27016, reload=True)
