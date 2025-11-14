from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "Dashboard API is running!"}

@app.get("/api/dashboard")
def dashboard():
    return {"dashboard": "this is dashboard endpoint!"}
