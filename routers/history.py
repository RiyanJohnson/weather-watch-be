from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from db.db import get_db
from models import HistoryEntry
from services import history as history_service

router = APIRouter(prefix="/history", tags=["History"])

@router.get("", response_model=List[HistoryEntry])
def get_history(db: Session = Depends(get_db)):
    return history_service.get_all(db)
