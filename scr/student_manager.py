def add_student(students, name, surname):
    """Adds a new student to the list."""
    new_id = students[-1][0] + 1 if students else 1
    students.append([new_id, name, surname, []])
    return f"Student added: {new_id} - {name} {surname}."

def display_students(students):
    """Displays the list of students and their attendance records."""
    print("\nStudent List:")
    for student in students:
        print(f"{student[0]} - {student[1]} {student[2]}")
        for entry in student[3]:
            print(f"  Date: {entry['data']} - Status: {entry['status']}")
    print()
