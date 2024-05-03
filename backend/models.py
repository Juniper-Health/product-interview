from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    insurance = relationship("Insurance", back_populates="patient", uselist=False)
    sessions = relationship("Session", back_populates="patient")


class Insurance(Base):
    __tablename__ = "insurance"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey(Patient.id))
    payer_name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    patient = relationship(Patient, back_populates="insurance", uselist=False)
    authorizations = relationship("Authorization", back_populates="insurance")


class Authorization(Base):
    __tablename__ = "authorization"
    id = Column(Integer, primary_key=True)
    insurance_id = Column(Integer, ForeignKey(Insurance.id))
    service_code = Column(String)
    units = Column(Integer)
    insurance = relationship(Insurance, back_populates="authorizations", uselist=False)


class Session(Base):
    __tablename__ = "session"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey(Patient.id))
    date = Column(Date)
    service_code = Column(String)
    units = Column(Integer)
    unit_charge = Column(Integer)
    patient = relationship(Patient, back_populates="sessions", uselist=False)
