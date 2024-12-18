import unittest
from datetime import datetime
from scr.attendance_manager import mark_attendance, update_attendance
from scr.file_operations import import_students, export_students
from scr.student_manager import add_student
import os

class TestAttendanceSystem(unittest.TestCase):
    def setUp(self):
        # Setup wspólnych danych dla wszystkich testów
        self.students = [
            [1, "John", "Doe", []],
            [2, "Jane", "Smith", []]
        ]
        self.file_name = "test_students.csv"

    def tearDown(self):
        # Usuwanie pliku po testach, jeśli istnieje
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    # Testy operacji na obecności
    def test_mark_attendance(self):
        date_str = "2024-12-18"
        result = mark_attendance(self.students, 1, "Present", date_str)
        self.assertEqual(result, "Attendance updated: 1 -> Present (2024-12-18)")
        self.assertEqual(self.students[0][3][0], {"data": date_str, "status": "Present"})

    def test_update_attendance(self):
        date_str = "2024-12-18"
        mark_attendance(self.students, 1, "Present", date_str)
        result = update_attendance(self.students, 1, "Absent", date_str)
        self.assertEqual(result, "Attendance updated for 1 on 2024-12-18.")
        self.assertEqual(self.students[0][3][0]["status"], "Absent")

    def test_mark_attendance_invalid_student(self):
        result = mark_attendance(self.students, 99, "Present")
        self.assertEqual(result, "Student ID 99 not found.")

    def test_update_attendance_no_record(self):
        result = update_attendance(self.students, 1, "Present", "2024-12-18")
        self.assertEqual(result, "No attendance record for 1 on 2024-12-18.")

    # Testy operacji na plikach
    def test_export_students(self):
        export_students(self.students, self.file_name)
        self.assertTrue(os.path.exists(self.file_name))

    def test_import_students(self):
        export_students(self.students, self.file_name)
        imported_students = import_students(self.file_name)
        self.assertEqual(len(imported_students), 2)
        self.assertEqual(imported_students[0][0], 1)
        self.assertEqual(imported_students[0][1], "John")

    # Testy operacji na studentach
    def test_add_student(self):
        result = add_student(self.students, "Alice", "Johnson")
        self.assertEqual(result, "Student added: 3 - Alice Johnson.")
        self.assertEqual(len(self.students), 3)
        self.assertEqual(self.students[-1], [3, "Alice", "Johnson", []])

if __name__ == "__main__":
    unittest.main()
