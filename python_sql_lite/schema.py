sql_create_doctors_table = """
    CREATE TABLE Doctors (
        DoctorID INT PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        Specialization VARCHAR(100),
        PhoneNumber VARCHAR(15)
    );
"""

sql_create_patients_table = """
    CREATE TABLE Patients (
        PatientID INT PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        DateOfBirth DATE,
        PhoneNumber VARCHAR(15)
    );
"""

sql_create_appointments_table = """
    CREATE TABLE Appointments (
        AppointmentID INT PRIMARY KEY,
        DoctorID INT,
        PatientID INT,
        AppointmentDate DATETIME,
        ReasonForVisit VARCHAR(255)
    );
"""

sql_create_prescriptions_table = """
    CREATE TABLE Prescriptions (
        PrescriptionID INT PRIMARY KEY,
        PatientID INT,
        DoctorID INT,
        Medication VARCHAR(100),
        Dosage VARCHAR(50),
        Instructions TEXT,
        PrescriptionDate DATE
    );
"""

sql_create_insurance_table = """
    CREATE TABLE InsuranceInformation (
        InsuranceID INT PRIMARY KEY,
        PatientID INT,
        InsuranceProvider VARCHAR(100),
        PolicyNumber VARCHAR(50),
        GroupNumber VARCHAR(50),
        PolicyHolderName VARCHAR(100),
        EffectiveDate DATE,
        ExpiryDate DATE
    );
"""

def get_schema():
    schema = f"{sql_create_doctors_table}{sql_create_patients_table}{sql_create_prescriptions_table}{sql_create_appointments_table}{sql_create_insurance_table}"
    return schema