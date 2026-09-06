from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from db.db import get_db
from models import Report
from services import reports as report_service

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("", response_model=List[Report])
def get_reports(db: Session = Depends(get_db)):
    return report_service.get_all(db)
