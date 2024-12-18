from datetime import datetime

def mark_attendance(students, student_id, attendance, date_str=None):
    """Marks attendance for a specific student."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')

    for student in students:
        if student[0] == student_id:
            student[3].append({'data': date_str, 'status': attendance})
            return f"Attendance updated: {student_id} -> {attendance} ({date_str})"
    return f"Student ID {student_id} not found."

def update_attendance(students, student_id, new_status, date_str):
    """Updates attendance status for a specific student on a specific date."""
    for student in students:
        if student[0] == student_id:
            for entry in student[3]:
                if entry['data'] == date_str:
                    entry['status'] = new_status
                    return f"Attendance updated for {student_id} on {date_str}."
            return f"No attendance record for {student_id} on {date_str}."
    return f"Student ID {student_id} not found."
