from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional
from datetime import datetime, date

class LabelData(BaseModel):
    labels: List[str]
    data: List[float]

class DashboardSummary(BaseModel):
    activeDisasters: int
    critical: int
    high: int
    medium: int
    populationAtRisk: int

class Analytics(BaseModel):
    disastersByType: LabelData
    severityDistribution: LabelData
    incidentsOverTime: LabelData
    populationAtRisk: LabelData
    responseStatus: LabelData

class Facility(BaseModel):
    id: str
    name: str
    type: str # Hospital, Shelter, Rescue Center
    latitude: float
    longitude: float

class HistoryEntry(BaseModel):
    date: date
    disaster: str
    location: str
    severity: str
    affectedArea: float
    status: str

class Report(BaseModel):
    id: str
    disasterType: str
    location: str
    submittedBy: str
    timeAgo: str
    status: str
    severity: str

class Alert(BaseModel):
    id: str
    title: str
    disasterId: str
    type: str
    severity: str
    location: str
    affectedArea: float
    populationAtRisk: int
    reportedMinutesAgo: int
    acknowledged: bool = False

class Disaster(BaseModel):
    id: str
    type: str
    location: str
    latitude: float
    longitude: float
    severity: str
    confidence: float
    affectedArea: float
    dryArea: float
    populationAtRisk: int
    status: str
    timestamp: datetime
    image: str
    reportedMinutesAgo: Optional[int] = None
    roadAccessibility: Optional[str] = None
    rainfall: Optional[str] = None
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    waterLevel: Optional[str] = None
    originalImage: Optional[str] = None
    segmentationImage: Optional[str] = None
    overlayImage: Optional[str] = None
    aiSummary: Optional[str] = None
    recommendations: Optional[List[str]] = None

class Error(BaseModel):
    detail: str
