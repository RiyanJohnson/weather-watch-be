from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from db.db import get_db
from models import Facility
from services import facilities as facility_service

router = APIRouter(prefix="/facilities", tags=["Facilities"])

@router.get("", response_model=List[Facility])
def get_facilities(db: Session = Depends(get_db)):
    return facility_service.get_all(db)
