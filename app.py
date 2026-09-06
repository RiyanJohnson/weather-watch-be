from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from db.db import engine, get_db, Base
from db.models import Test
from routers import disasters, alerts, reports, history, facilities, dashboard, ai_pipeline

app = FastAPI(title="RescueAI — Disaster Response Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(disasters.router)
app.include_router(alerts.router)
app.include_router(reports.router)
app.include_router(history.router)
app.include_router(facilities.router)
app.include_router(dashboard.router)
app.include_router(ai_pipeline.router)

@app.post("/test")
def add_test(name: str, db: Session = Depends(get_db)):
    data = Test(name=name)

    db.add(data)
    db.commit()
    db.refresh(data)

    return data

@app.get("/test")
def get_test(db: Session = Depends(get_db)):
    return db.query(Test).all()
