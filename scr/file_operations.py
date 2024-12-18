import csv

def import_students(file_name="students_list.csv"):
    """Imports student data from a CSV file."""
    students = []
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                # Format: id, name, surname, attendance (optional)
                students.append([int(row[0]), row[1], row[2], []])
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty list.")
    return students

def export_students(students, file_name="students_list.csv"):
    """Exports student data to a CSV file."""
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "surname", "attendance"])
        for student in students:
            writer.writerow([
                student[0], 
                student[1], 
                student[2], 
                ";".join([f"{entry['data']}:{entry['status']}" for entry in student[3]])
            ])
    print(f"Student data saved to '{file_name}'.")

