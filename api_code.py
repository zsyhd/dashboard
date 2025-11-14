from fastapi import FastAPI

app = FastAPI()

@app.get("/api/dashboard")
def get_dashboard():
    return {
        "summary": {
            "totalEvents": 6,
            "wellCount": 6,
            "anomalyRate": 0.46,
            "avgPressure": 78.9
        },
        "wells": [
            "W1",
            "W2",
            "W3"
        ],
        "eventTypes": [
            "Flow",
            "Pressure",
            "Temperature"
        ],
        "events": {
            "items": [
                {
                    "id": 1012,
                    "at": "2025-07-12T09:13:00Z",
                    "date": "2025-07-12",
                    "well": "W1",
                    "type": "Flow",
                    "severity": "none",
                    "isAnomaly": False,
                    "value": 92.7,
                    "features": "p-pdg",
                    "meta": {
                        "unit": "psi",
                        "threshold": 80
                    },
                    "read": True
                }
            ],
            "page": 0,
            "pageSize": 0,
            "total": 0
        },
        "timeseries": {
            "granularity": "day",
            "points": [
                {
                    "name": "Jan",
                    "values": {
                        "P-PDG": 70,
                        "P-TPT": 40,
                        "T-TPT": 10
                    }
                }
            ]
        },
        "anomalyDistribution": {
            "items": [
                {
                    "name": "Normal",
                    "value": 45,
                    "color": "#00C49F"
                }
            ]
        },
        "failureCards": {
            "items": [
                {
                    "label":
