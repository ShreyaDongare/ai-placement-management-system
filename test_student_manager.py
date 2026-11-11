import unittest

from student_manager import StudentManager

class TestStudentManager(unittest.TestCase):

    def setUp(self):
        self.manager = StudentManager()
        
    def test_register_student(self):

        student = self.manager.register_student(
            "101",
            "Shreya",
            "shreya@example.com"
        )

        self.assertEqual(student.name, "Shreya")
        
    def test_duplicate_registration(self):
        
        self.manager.register_student(
            "101",
            "Shreya",
            "shreya@example.com"
        )

        with self.assertRaises(ValueError):

            self.manager.register_student(
                "101",
                "Aarav",
                "aarav@example.com"
            )

    def test_update_student(self):

        self.manager.register_student(
            "101",
            "Shreya",
            "shreya@example.com"
        )

        self.manager.update_student("101", name="Shreya D")

        student = self.manager.get_student("101")

        self.assertEqual(student.name, "Shreya D")

    def test_student_not_found(self):

        with self.assertRaises(KeyError):
            self.manager.get_student("999")

if __name__ == "__main__":
    unittest.main()