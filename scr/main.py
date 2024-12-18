from scr.file_operations import import_students, export_students
from scr.attendance_manager import mark_attendance, update_attendance
from scr.student_manager import add_student, display_students

def main():
    file_name = "students_list.csv"
    students = import_students(file_name)

    while True:
        print("\n1. Display students")
        print("2. Add a student")
        print("3. Mark attendance")
        print("4. Update attendance")
        print("5. Save and exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_students(students)
        elif choice == "2":
            name = input("Enter student's first name: ")
            surname = input("Enter student's last name: ")
            print(add_student(students, name, surname))
        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            attendance = input("Enter attendance status (Present/Absent): ")
            print(mark_attendance(students, student_id, attendance))
        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            date_str = input("Enter date (YYYY-MM-DD): ")
            new_status = input("Enter new attendance status (Present/Absent): ")
            print(update_attendance(students, student_id, new_status, date_str))
        elif choice == "5":
            export_students(students, file_name)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
