from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# افزودن CORS (اگر قبلاً اضافه نکرده‌اید)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تغییر مسیر اصلی (Root Path)
# تابع get_dashboard را به مسیر اصلی ("/") متصل می‌کنیم.
@app.get("/")
def get_dashboard():
    # این همان کدی است که قبلاً در مسیر /api/dashboard بود.
    # حالا به مسیر اصلی منتقل شده است.
    return {
        "summary": {
            "totalEvents": 6,
            "wellCount": 6,
            "anomalyRate": 0.46,
            "avgPressure": 78.9
        },
        "status": "OK",
        "note": "This is the actual dashboard data now on the root path."
    }

# اگر مسیر /api/dashboard را هم می‌خواهید نگه دارید، آن را هم تعریف کنید:
@app.get("/api/dashboard")
def get_dashboard_api():
    return get_dashboard() # از همان تابع استفاده می‌کنیم
