import os

from db import create_table, create_connection
from schema import *

def insert_to_doctors(conn):
    sql = """
        INSERT INTO Doctors VALUES
            (1, 'John', 'Smith', 'Cardiologist', '555-123-4567'),
            (2, 'Emily', 'Johnson', 'Pediatrician', '555-987-6543'),
            (3, 'Michael', 'Davis', 'Dermatologist', '555-555-5555'),
            (4, 'Susan', 'Williams', 'Orthopedic Surgeon', '555-333-7890'),
            (5, 'David', 'Lee', 'Ophthalmologist', '555-444-5678'),
            (6, 'Jennifer', 'Brown', 'Gynecologist', '555-555-1234'),
            (7, 'Richard', 'Martin', 'Neurologist', '555-222-9876'),
            (8, 'Karen', 'Anderson', 'ENT Specialist', '555-777-2345'),
            (9, 'Thomas', 'Clark', 'Urologist', '555-888-4567'),
            (10, 'Laura', 'Hall', 'Psychiatrist', '555-666-3456'),
            (11, 'William', 'Garcia', 'Dentist', '555-555-1111'),
            (12, 'Mary', 'Harris', 'Family Physician', '555-999-7890'),
            (13, 'Robert', 'Taylor', 'Dermatologist', '555-222-5678'),
            (14, 'Jessica', 'Moore', 'Cardiologist', '555-444-6789'),
            (15, 'Daniel', 'White', 'Pediatrician', '555-333-1234'),
            (16, 'Megan', 'Young', 'Orthopedic Surgeon', '555-888-9876'),
            (17, 'James', 'Lopez', 'Gynecologist', '555-777-5678'),
            (18, 'Emily', 'Parker', 'Neurologist', '555-999-3456'),
            (19, 'Christopher', 'Smith', 'ENT Specialist', '555-222-1234'),
            (20, 'Olivia', 'Davis', 'Urologist', '555-333-2345'),
            (21, 'Sophia', 'Wilson', 'Psychiatrist', '555-666-4567'),
            (22, 'Aiden', 'Johnson', 'Dentist', '555-555-5678'),
            (23, 'Ava', 'Martinez', 'Family Physician', '555-444-7890');
            """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_patients(conn):

    sql = """
        INSERT INTO Patients (PatientID, FirstName, LastName, DateOfBirth, PhoneNumber)
        VALUES
        (101, 'Sarah', 'Wilson', '1990-03-15', '555-111-2222'),
        (102, 'Robert', 'Jones', '1985-07-22', '555-333-4444'),
        (103, 'Linda', 'Brown', '2000-12-10', '555-555-5555'),
        (104, 'Daniel', 'Turner', '1978-09-25', '555-111-3456'),
        (105, 'Olivia', 'Gonzalez', '1995-02-18', '555-333-5678'),
        (106, 'Sophia', 'Roberts', '1982-07-30', '555-777-6789'),
        (107, 'Ethan', 'Hernandez', '2005-05-12', '555-444-7890'),
        (108, 'Isabella', 'Hall', '1998-11-03', '555-888-8901'),
        (109, 'Aiden', 'Young', '2002-03-08', '555-555-1234'),
        (110, 'Mia', 'King', '1990-12-15', '555-666-2345'),
        (111, 'Liam', 'Miller', '2008-04-01', '555-222-3456'),
        (112, 'Charlotte', 'Anderson', '2000-08-20', '555-333-4567'),
        (113, 'Noah', 'Brown', '1989-01-05', '555-777-5678'),
        (114, 'Ava', 'Davis', '1976-06-10', '555-555-6789'),
        (115, 'William', 'Jackson', '2001-09-28', '555-888-7890'),
        (116, 'Emily', 'Thomas', '1993-03-19', '555-111-8901'),
        (117, 'James', 'White', '1999-12-07', '555-222-1234'),
        (118, 'Abigail', 'Moore', '2003-10-14', '555-444-2345'),
        (119, 'Benjamin', 'Clark', '1997-07-02', '555-777-3456'),
        (120, 'Sofia', 'Taylor', '1985-04-26', '555-666-4567'),
        (121, 'Henry', 'Carter', '2010-02-22', '555-555-5678'),
        (122, 'Emma', 'Johnson', '1992-06-09', '555-888-6789'),
        (123, 'Alexander', 'Wilson', '1994-08-14', '555-333-7890');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_appointments(conn):

    sql = """
        INSERT INTO Appointments (AppointmentID, DoctorID, PatientID, AppointmentDate, ReasonForVisit)
        VALUES
        (1001, 1, 101, '2023-10-10 09:30:00', 'Annual checkup'),
        (1002, 2, 102, '2023-10-12 14:00:00', 'Vaccination'),
        (1003, 3, 103, '2023-10-15 11:15:00', 'Skin rash'),
        (1004, 4, 104, '2023-10-18 10:30:00', 'Knee pain evaluation'),
        (1005, 5, 105, '2023-10-20 15:45:00', 'Eye exam'),
        (1006, 6, 106, '2023-10-25 09:15:00', 'Prenatal checkup'),
        (1007, 7, 107, '2023-10-28 14:30:00', 'Headache consultation'),
        (1008, 8, 108, '2023-11-02 11:00:00', 'Ear infection'),
        (1009, 9, 109, '2023-11-05 16:00:00', 'Urinary tract infection'),
        (1010, 10, 110, '2023-11-10 08:45:00', 'Counseling session'),
        (1011, 11, 111, '2023-11-12 13:30:00', 'Dental cleaning'),
        (1012, 12, 112, '2023-11-15 10:15:00', 'Annual physical'),
        (1013, 13, 113, '2023-11-20 14:00:00', 'Acne treatment'),
        (1014, 14, 114, '2023-11-22 09:00:00', 'Heart checkup'),
        (1015, 15, 115, '2023-11-25 15:15:00', 'Pediatric vaccination'),
        (1016, 16, 116, '2023-11-28 11:30:00', 'Orthopedic consultation'),
        (1017, 17, 117, '2023-12-02 14:45:00', 'Neurology follow-up'),
        (1018, 18, 118, '2023-12-05 10:00:00', 'ENT examination'),
        (1019, 19, 119, '2023-12-10 16:30:00', 'Urology checkup'),
        (1020, 20, 120, '2023-12-12 08:15:00', 'Psychiatric evaluation'),
        (1021, 21, 121, '2023-12-15 13:00:00', 'Dental checkup'),
        (1022, 22, 122, '2023-12-18 09:45:00', 'Family medicine consultation'),
        (1023, 23, 123, '2023-12-20 15:30:00', 'Skin condition assessment'),
        (1024, 1, 104, '2023-12-25 10:00:00', 'Follow-up on knee pain'),
        (1025, 2, 105, '2023-12-28 14:15:00', 'Eye prescription update'),
        (1026, 3, 106, '2023-12-30 09:30:00', 'Prenatal ultrasound'),
        (1027, 4, 107, '2024-01-05 11:45:00', 'Headache follow-up'),
        (1028, 5, 108, '2024-01-08 16:30:00', 'Earache assessment'),
        (1029, 6, 109, '2024-01-10 13:00:00', 'UTI follow-up'),
        (1030, 7, 110, '2024-01-15 15:45:00', 'Therapy session'),
        (1031, 8, 111, '2024-01-18 10:30:00', 'Dental filling'),
        (1032, 9, 112, '2024-01-20 14:00:00', 'Follow-up on physical'),
        (1033, 10, 113, '2024-01-25 09:15:00', 'Acne checkup'),
        (1034, 11, 114, '2024-01-28 16:00:00', 'Cardiac stress test');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_prescriptions(conn):
    sql = """
        INSERT INTO Prescriptions (PrescriptionID, PatientID, DoctorID, Medication, Dosage, Instructions, PrescriptionDate)
        VALUES
        (2001, 101, 1, 'Lipitor', '10mg', 'Take once daily with food', '2023-10-10'),
        (2002, 102, 2, 'Pediarix', '2.5mL', 'Administer as directed', '2023-10-12'),
        (2003, 103, 3, 'Cortisone Cream', 'Apply to affected area', 'Apply twice daily', '2023-10-15'),
        (2004, 104, 4, 'Ibuprofen', '400mg', 'Take as needed for pain', '2023-10-18'),
        (2005, 105, 5, 'Latanoprost', '1 drop in each eye at bedtime', 'Apply daily', '2023-10-20'),
        (2006, 106, 6, 'Prenatal vitamins', '1 tablet daily', 'Take with food', '2023-10-25'),
        (2007, 107, 7, 'Sumatriptan', '50mg', 'Take at onset of headache', '2023-10-28'),
        (2008, 108, 8, 'Amoxicillin', '500mg', 'Take as prescribed', '2023-11-02'),
        (2009, 109, 9, 'Ciprofloxacin', '250mg', 'Take twice daily', '2023-11-05'),
        (2010, 110, 10, 'Fluoxetine', '20mg', 'Take daily in the morning', '2023-11-10'),
        (2011, 111, 11, 'Fluoride toothpaste', 'Use pea-sized amount', 'Brush teeth twice daily', '2023-11-12'),
        (2012, 112, 12, 'Aspirin', '81mg', 'Take daily with water', '2023-11-15'),
        (2013, 113, 13, 'Tretinoin cream', 'Apply to affected area', 'Apply at bedtime', '2023-11-20'),
        (2014, 114, 14, 'Metoprolol', '25mg', 'Take twice daily with food', '2023-11-22'),
        (2015, 115, 15, 'DTaP vaccine', 'As per schedule', 'Administer as directed', '2023-11-25'),
        (2016, 116, 16, 'Naproxen', '250mg', 'Take as needed for pain', '2023-11-28'),
        (2017, 117, 17, 'Topiramate', '50mg', 'Take at bedtime', '2023-12-02'),
        (2018, 118, 18, 'Nasal spray', 'As directed', 'Administer as needed', '2023-12-05'),
        (2019, 119, 19, 'Nitrofurantoin', '100mg', 'Take with food', '2023-12-10'),
        (2020, 120, 20, 'Sertraline', '50mg', 'Take daily in the morning', '2023-12-12'),
        (2021, 121, 21, 'Fluoride mouthwash', 'Use as directed', 'Rinse mouth daily', '2023-12-15'),
        (2022, 122, 22, 'Multivitamin', '1 tablet daily', 'Take with breakfast', '2023-12-18'),
        (2023, 123, 23, 'Hydrocortisone cream', 'Apply to affected area', 'Apply as needed', '2023-12-20'),
        (2024, 1, 104, 'Acetaminophen', '500mg', 'Take as needed for pain', '2023-12-25'),
        (2025, 2, 105, 'Atropine eye drops', '1 drop in each eye', 'Use as directed', '2023-12-28');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_insurance(conn):
    sql = """
        INSERT INTO InsuranceInformation (InsuranceID, PatientID, InsuranceProvider, PolicyNumber, GroupNumber, PolicyHolderName, EffectiveDate, ExpiryDate)
        VALUES
        (3001, 101, 'BlueCross', 'BC12345', 'G1234', 'Sarah Wilson', '2023-01-01', '2023-12-31'),
        (3002, 102, 'Aetna', 'A78901', 'A5678', 'Robert Jones', '2023-03-15', '2023-12-31'),
        (3003, 103, 'Cigna', 'C45678', 'C123', 'Linda Brown', '2023-02-10', '2023-12-31'),
        (3004, 104, 'UnitedHealthcare', 'UH56789', 'U9876', 'Daniel Turner', '2023-05-20', '2023-12-31'),
        (3005, 105, 'BlueCross', 'BC67890', 'B5678', 'Olivia Gonzalez', '2023-04-01', '2023-12-31'),
        (3006, 106, 'Aetna', 'A12345', 'A2345', 'Sophia Roberts', '2023-06-30', '2023-12-31'),
        (3007, 107, 'Cigna', 'C23456', 'C5678', 'Ethan Hernandez', '2023-09-12', '2023-12-31'),
        (3008, 108, 'UnitedHealthcare', 'UH12345', 'U5678', 'Isabella Hall', '2023-07-05', '2023-12-31'),
        (3009, 109, 'BlueCross', 'BC34567', 'B1234', 'Aiden Young', '2023-08-18', '2023-12-31'),
        (3010, 110, 'Aetna', 'A56789', 'A6789', 'Mia King', '2023-10-25', '2023-12-31'),
        (3011, 111, 'Cigna', 'C67890', 'C1234', 'Liam Miller', '2023-12-05', '2023-12-31'),
        (3012, 112, 'UnitedHealthcare', 'UH23456', 'U6789', 'Charlotte Anderson', '2023-11-15', '2023-12-31'),
        (3013, 113, 'BlueCross', 'BC78901', 'B5678', 'Noah Brown', '2023-07-28', '2023-12-31'),
        (3014, 114, 'Aetna', 'A23456', 'A3456', 'Ava Davis', '2023-09-03', '2023-12-31'),
        (3015, 115, 'Cigna', 'C34567', 'C4567', 'William Jackson', '2023-02-14', '2023-12-31'),
        (3016, 116, 'UnitedHealthcare', 'UH34567', 'U4567', 'Emily Thomas', '2023-06-18', '2023-12-31'),
        (3017, 117, 'BlueCross', 'BC23456', 'B3456', 'James White', '2023-08-22', '2023-12-31'),
        (3018, 118, 'Aetna', 'A34567', 'A4567', 'Abigail Moore', '2023-10-02', '2023-12-31'),
        (3019, 119, 'Cigna', 'C12345', 'C2345', 'Benjamin Clark', '2023-11-30', '2023-12-31'),
        (3020, 120, 'UnitedHealthcare', 'UH78901', 'U5678', 'Sofia Taylor', '2023-12-12', '2023-12-31');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def main():
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    create_table(conn, sql_create_doctors_table)
    insert_to_doctors(conn)
    create_table(conn, sql_create_prescriptions_table)
    insert_to_prescriptions(conn)
    create_table(conn, sql_create_patients_table)
    insert_to_patients(conn)
    create_table(conn, sql_create_appointments_table)
    insert_to_appointments(conn)
    create_table(conn, sql_create_insurance_table)
    insert_to_insurance(conn)

    print("Database build successful!")

if __name__ == "__main__":
    main()
