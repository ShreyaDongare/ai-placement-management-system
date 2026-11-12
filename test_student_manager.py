import unittest
import tempfile
from pathlib import Path

from student_manager import StudentManager

class TestStudentManager(unittest.TestCase):

    def setUp(self):
        # Create a separate temporary directory for each test
        self.temp_dir = tempfile.TemporaryDirectory()

        # Store test JSON inside the temporary directory
        self.file_path = Path(self.temp_dir.name) / "students.json"

        # Each test gets its own StudentManager
        self.manager = StudentManager(file_path=self.file_path)

    def tearDown(self):
        # Remove temporary files after every test
        self.temp_dir.cleanup()

    def test_register_student(self):
        student = self.manager.register_student(
            "101", "Shreya", "shreya@example.com"
        )

        self.assertEqual(student.name, "Shreya")

    def test_duplicate_registration(self):
        self.manager.register_student(
            "101", "Shreya", "shreya@example.com"
        )

        with self.assertRaises(ValueError):
            self.manager.register_student(
                "101", "Aarav", "aarav@example.com"
            )

    def test_update_student(self):
        self.manager.register_student(
            "101", "Shreya", "shreya@example.com"
        )

        self.manager.update_student("101", name="Shreya D")

        student = self.manager.get_student("101")

        self.assertEqual(student.name, "Shreya D")

    def test_student_not_found(self):
        with self.assertRaises(KeyError):
            self.manager.get_student("999")

    def test_student_persistence(self):
        # Register a student
        self.manager.register_student(
            "101", "Shreya", "shreya@example.com"
        )

        # Create a new manager using the same JSON file
        new_manager = StudentManager(file_path=self.file_path)

        # Check whether student data was loaded
        student = new_manager.get_student("101")

        self.assertEqual(student.name, "Shreya")
        self.assertEqual(student.email, "shreya@example.com")

    def test_missing_json_file(self):
        # A missing JSON file should start with an empty collection
        self.assertEqual(self.manager.list_students(), [])

if __name__ == "__main__":
    unittest.main()