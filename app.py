from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.db import engine, get_db, Base
from db.models import Test

app = FastAPI()

Base.metadata.create_all(bind=engine)

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