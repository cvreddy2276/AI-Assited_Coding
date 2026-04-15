"""
attendance.py
Attendance Management Module
"""

_attendance_record = {}

def mark_present(student):
    """
    Mark the given student as present.
    Args:
        student (str): The name or ID of the student.
    """
    _attendance_record[student] = 'Present'

def mark_absent(student):
    """
    Mark the given student as absent.
    Args:
        student (str): The name or ID of the student.
    """
    _attendance_record[student] = 'Absent'

def get_attendance(student):
    """
    Get the attendance status of the given student.
    Args:
        student (str): The name or ID of the student.
    Returns:
        str: 'Present', 'Absent', or 'Not Marked'.
    """
    return _attendance_record.get(student, 'Not Marked')
