import csv
import random
import sqlite3
from datetime import date

from faker import Faker

from main import get_db
from models import Authorization, Insurance, Patient, Session

fake = Faker()

conn = sqlite3.connect("./data.db")
cursor = conn.cursor()

drop_table_query = "DROP TABLE IF EXISTS session;"
cursor.execute(drop_table_query)
drop_table_query = "DROP TABLE IF EXISTS authorization;"
cursor.execute(drop_table_query)
drop_table_query = "DROP TABLE IF EXISTS insurance;"
cursor.execute(drop_table_query)
drop_table_query = "DROP TABLE IF EXISTS patient;"
cursor.execute(drop_table_query)
conn.commit()

# Define the CREATE TABLE statement
create_table_query = """
CREATE TABLE IF NOT EXISTS patient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
"""
cursor.execute(create_table_query)
create_table_query = """
CREATE TABLE IF NOT EXISTS insurance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    payer_name TEXT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patient(id)
);
"""
cursor.execute(create_table_query)
create_table_query = """
CREATE TABLE IF NOT EXISTS authorization (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    insurance_id INTEGER,
    service_code TEXT,
    units INTEGER,
    FOREIGN KEY (insurance_id) REFERENCES insurance(id)
);
"""
cursor.execute(create_table_query)
create_table_query = """
CREATE TABLE IF NOT EXISTS session (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    date DATE,
    service_code TEXT,
    units INTEGER,
    unit_charge INTEGER,
    FOREIGN KEY (patient_id) REFERENCES patient(id)
);
"""
cursor.execute(create_table_query)

conn.commit()
conn.close()

session = next(get_db())
with open("./data/patient.csv") as csvfile:
    file = csv.DictReader(csvfile)
    for row in file:
        session.add(Patient(id=row["id"], name=row["name"]))
    session.commit()

patients = session.query(Patient).order_by(Patient.id).all()
for index, patient in enumerate(patients):
    index = index + 1
    start_date = fake.date_between(date(2023, 1, 1), date(2023, 3, 1))
    end_date = fake.date_between(start_date, date(2023, 12, 31))
    insurance = Insurance(
        id=index,
        patient_id=patient.id,
        payer_name=random.choice(["Blue Cross", "Aetna", "Cigna"]),
        start_date=start_date,
        end_date=end_date,
    )
    session.add(insurance)

    authorization = Authorization(
        insurance_id=index, service_code="97151", units=fake.random_int(1, 4)
    )
    session.add(authorization)
    authorization = Authorization(
        insurance_id=index, service_code="97153", units=fake.random_int(20, 70)
    )
    session.add(authorization)

    for x in range(1, 13):
        session.add(
            Session(
                patient_id=index,
                date=date(2023, x, 1),
                service_code="97151",
                units=1,
                unit_charge=fake.random_int(100, 200),
            )
        )
        for y in range(1, 5):
            session.add(
                Session(
                    patient_id=index,
                    date=date(2023, x, y * 7),
                    service_code="97153",
                    units=random.choice([1, 2, 3]),
                    unit_charge=fake.random_int(100, 200),
                )
            )
session.commit()
