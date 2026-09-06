from db.db import SessionLocal
from db.models import DisasterModel, AlertModel, ReportModel, HistoryEntryModel, FacilityModel

def clear_db():
    db = SessionLocal()
    try:
        db.query(DisasterModel).delete()
        db.query(AlertModel).delete()
        db.query(FacilityModel).delete()
        db.query(ReportModel).delete()
        db.query(HistoryEntryModel).delete()
        db.commit()
        print("Database successfully cleared of mock data.")
    except Exception as e:
        db.rollback()
        print("Failed to clear database:", e)
    finally:
        db.close()

if __name__ == "__main__":
    clear_db()
