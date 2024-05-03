from datetime import date

from pydantic import BaseModel, ConfigDict


class FromAttributesModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class PatientResponse(FromAttributesModel):
    id: int
    name: str


class InsuranceResponse(FromAttributesModel):
    id: int
    patient_id: int
    payer_name: str
    start_date: date
    end_date: date


class AuthorizationResponse(FromAttributesModel):
    id: int
    insurance_id: int
    service_code: str
    units: int


class SessionResponse(FromAttributesModel):
    id: int
    patient_id: int
    date: date
    service_code: str
    units: int
    unit_charge: int
