from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.db import get_db
from models import Alert, AlertCreate, Error
from services import alerts as alert_service

router = APIRouter(prefix="/alerts", tags=["Alerts"])

@router.get("", response_model=List[Alert])
def get_alerts(db: Session = Depends(get_db)):
    return alert_service.get_all(db)

@router.post("", response_model=Alert, status_code=201)
def create_alert(body: AlertCreate, db: Session = Depends(get_db)):
    return alert_service.create(db, body.model_dump())

@router.post("/{id}/acknowledge", responses={404: {"model": Error}})
def acknowledge_alert(id: str, db: Session = Depends(get_db)):
    alert = alert_service.acknowledge(db, id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {"success": True, "id": id}
