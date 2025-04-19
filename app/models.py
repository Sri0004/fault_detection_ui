from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class FaultDetection(Base):
    __tablename__ = "faults"

    id = Column(Integer, primary_key=True, index=True)
    sensor_name = Column(String, index=True)
    fault_type = Column(String)
    confidence_score = Column(Float)

