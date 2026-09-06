from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from db.db import get_db
from models import Disaster, Error
from services import disasters as disaster_service

router = APIRouter(prefix="/disasters", tags=["Disasters"])

@router.get("", response_model=List[Disaster])
def get_disasters(
    severity: Optional[str] = Query(None, enum=["Critical", "High", "Medium", "Low"]),
    type: Optional[str] = Query(None, enum=["Flood", "Fire", "Smoke", "Landslide", "Building Collapse", "Road Blockage"]),
    status: Optional[str] = Query(None, enum=["Active", "Monitoring", "Resolved"]),
    db: Session = Depends(get_db)
):
    return disaster_service.get_all(db, severity, type, status)

@router.get("/{id}", response_model=Disaster, responses={404: {"model": Error}})
def get_disaster(id: str, db: Session = Depends(get_db)):
    disaster = disaster_service.get_by_id(db, id)
    if not disaster:
        raise HTTPException(status_code=404, detail="Disaster not found")
    return disaster
