from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db
from models import Analytics, DashboardSummary
from services import dashboard as dashboard_service

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("", response_model=Analytics)
def get_analytics(db: Session = Depends(get_db)):
    return dashboard_service.get_analytics(db)

@router.get("/summary", response_model=DashboardSummary)
def get_dashboard_summary(db: Session = Depends(get_db)):
    return dashboard_service.get_summary(db)
