-- Hospital Management System Schema and Queries
-- Using SQLite3
-- Normalized to 3NF: Specialty table separated to avoid redundancy

-- Create Specialty table
CREATE TABLE specialty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Create Doctor table
CREATE TABLE doctor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty_id INTEGER,
    phone TEXT,
    email TEXT UNIQUE,
    FOREIGN KEY (specialty_id) REFERENCES specialty(id)
);

-- Create Patients table
CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dob DATE,
    phone TEXT,
    email TEXT UNIQUE,
    address TEXT,
    CHECK (dob IS NULL OR dob <= date('now'))
);

-- Create Appointments table
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME,
    reason TEXT,
    status TEXT DEFAULT 'scheduled',
    FOREIGN KEY (doctor_id) REFERENCES doctor(id),
    FOREIGN KEY (patient_id) REFERENCES patients(id),
    CHECK (status IN ('scheduled', 'completed', 'cancelled'))
);

-- Query 1: List all appointments for a specific doctor
-- Replace ? with the actual doctor ID
SELECT a.id, a.appointment_date, a.appointment_time, a.reason, a.status,
       p.name AS patient_name, p.phone AS patient_phone, s.name AS specialty
FROM appointments a
JOIN patients p ON a.patient_id = p.id
JOIN doctor d ON a.doctor_id = d.id
JOIN specialty s ON d.specialty_id = s.id
WHERE a.doctor_id = ?
ORDER BY a.appointment_date, a.appointment_time;

-- Query 2: Retrieve patient history by patient ID
-- Replace ? with the actual patient ID
SELECT a.id, a.appointment_date, a.appointment_time, a.reason, a.status,
       d.name AS doctor_name, s.name AS specialty
FROM appointments a
JOIN doctor d ON a.doctor_id = d.id
JOIN specialty s ON d.specialty_id = s.id
WHERE a.patient_id = ?
ORDER BY a.appointment_date DESC;

-- Query 3: Count total patients treated by each doctor
SELECT d.name AS doctor_name, s.name AS specialty, COUNT(DISTINCT a.patient_id) AS total_patients
FROM doctor d
LEFT JOIN appointments a ON d.id = a.doctor_id
LEFT JOIN specialty s ON d.specialty_id = s.id
GROUP BY d.id, d.name, s.name
ORDER BY total_patients DESC;