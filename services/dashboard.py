from sqlalchemy.orm import Session
from models import Analytics, DashboardSummary, LabelData
from db.models import DisasterModel, AlertModel

def get_analytics(db: Session) -> Analytics:
    return Analytics(
        disastersByType=LabelData(labels=[], data=[]),
        severityDistribution=LabelData(labels=[], data=[]),
        incidentsOverTime=LabelData(labels=[], data=[]),
        populationAtRisk=LabelData(labels=[], data=[]),
        responseStatus=LabelData(labels=[], data=[])
    )

def get_summary(db: Session) -> DashboardSummary:
    return DashboardSummary(
        activeDisasters=0,
        critical=0,
        high=0,
        medium=0,
        populationAtRisk=0
    )
