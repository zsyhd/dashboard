from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_dashboard():
    return {
        "summary": {
            "totalEvents": 6,
            "wellCount": 6,
            "anomalyRate": 0.46,
            "avgPressure": 78.9
        },
        "status": "OK"
    }
