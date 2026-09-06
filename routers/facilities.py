from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from db.db import get_db
from models import Facility, FacilityCreate
from services import facilities as facility_service

router = APIRouter(prefix="/facilities", tags=["Facilities"])

@router.get("", response_model=List[Facility])
def get_facilities(db: Session = Depends(get_db)):
    return facility_service.get_all(db)

@router.post("", response_model=Facility, status_code=201)
def create_facility(body: FacilityCreate, db: Session = Depends(get_db)):
    return facility_service.create(db, body.model_dump())
