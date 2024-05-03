from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Authorization, Insurance, Patient, Session
from schemas import (
    AuthorizationResponse,
    InsuranceResponse,
    PatientResponse,
    SessionResponse,
)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./data.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Initialize FastAPI app
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint for Patient
@app.get("/patients/", response_model=List[PatientResponse])
def read_patients(db=Depends(get_db)):
    patients = db.query(Patient).all()
    return patients


# Endpoint for Insurance
@app.get("/insurances/", response_model=List[InsuranceResponse])
def read_insurances(db=Depends(get_db)):
    insurances = db.query(Insurance).all()
    return insurances


# Endpoint for Authorization
@app.get("/authorizations/", response_model=List[AuthorizationResponse])
def read_authorizations(db=Depends(get_db)):
    authorizations = db.query(Authorization).all()
    return authorizations


# Endpoint for Session
@app.get("/sessions/", response_model=List[SessionResponse])
def read_sessions(db=Depends(get_db)):
    sessions = db.query(Session).all()
    return sessions
