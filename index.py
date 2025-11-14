# محتوای index.py
from fastapi import FastAPI

app = FastAPI() # این خط حیاتی است!

@app.get("/")
def read_root():
    return {"Hello": "World"}

# ... بقیه کدهای مسیردهی (Routes) شما در اینجا قرار می‌گیرد ...
