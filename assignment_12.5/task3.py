# Task Description #3: Smart Healthcare Appointment Scheduling System
# A healthcare platform maintains appointment records containing
# appointment ID, patient name, doctor name, appointment time, and
# consultation fee. The system needs to:
# 1. Search appointments using appointment ID.
# 2. Sort appointments based on time or consultation fee.
# recommend suitable searching and sorting algorithms.
# • Implement the algorithms in Python.
def search_appointment(appointments, appointment_id):
    for appointment in appointments:
        if appointment['appointment_id'] == appointment_id:
            return appointment
    return None
def sort_appointments_by_time(appointments):
    return sorted(appointments, key=lambda x: x['appointment_time'])

def sort_appointments_by_fee(appointments):
    return sorted(appointments, key=lambda x: x['consultation_fee'])
# Example usage
appointments = [
    {'appointment_id': 'A001', 'patient_name': 'John Doe', 'doctor_name': 'Dr. Smith', 'appointment_time': '2024-07-01 10:00', 'consultation_fee': 100},    
]
# Search for an appointment
appointment_id = 'A001'
result = search_appointment(appointments, appointment_id)
if result:
    print(f"Appointment found: {result}")
else:
    print("Appointment not found.")
# Sort appointments by time
sorted_by_time = sort_appointments_by_time(appointments)
print("Appointments sorted by time:")
for appointment in sorted_by_time:
    print(appointment)
# Sort appointments by consultation fee
sorted_by_fee = sort_appointments_by_fee(appointments)
print("Appointments sorted by consultation fee:")
for appointment in sorted_by_fee:
    print(appointment)
