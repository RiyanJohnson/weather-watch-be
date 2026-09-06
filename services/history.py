from sqlalchemy.orm import Session
from db.models import HistoryEntryModel

def get_all(db: Session):
    return db.query(HistoryEntryModel).all()
