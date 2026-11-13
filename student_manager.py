import json
from pathlib import Path

class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email

    def update_profile(self, name=None, email=None):
        if name is not None:
            if not name.strip():
                raise ValueError("Name cannot be empty")
            self.name = name.strip()

        if email is not None:
            if not email.strip():
                raise ValueError("Email cannot be empty")
            self.email = email.strip()
            
    def display(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Email:", self.email)
        
    # Convert Student object into a dictionary
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email
        }
        
class StudentManager:

    def __init__(self, file_path= "students.json"):
        self.students = {}
        self.file_path = Path(file_path)
        
        self.load_students()
        
    def save_students(self):
        data = [
            student.to_dict()
            for student in self.students.values()
        ]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            
    # Load student records from JSON
    def load_students(self):
        if not self.file_path.exists():
            self.students = {}
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

        except json.JSONDecodeError as error:
            raise ValueError(
                "students.json contains invalid JSON. "
                "Please check the file before continuing."
            ) from error

        if not isinstance(data, list):
            raise ValueError("Student data must be a JSON list.")

        loaded_students = {}

        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Invalid student record in JSON.")

            try:
                student = Student(
                    item["student_id"],
                    item["name"],
                    item["email"]
                )
            except KeyError as error:
                raise ValueError(
                    f"Student record is missing field: {error}"
                ) from error

            if student.student_id in loaded_students:
                raise ValueError("Duplicate student ID in JSON.")

            loaded_students[student.student_id] = student

        # Replace current collection after successful loading
        self.students = loaded_students
        
    def register_student(self, student_id, name, email):

        student_id = student_id.strip()
        name = name.strip()
        email = email.strip()

        if not student_id or not name or not email:
            raise ValueError("All fields are required")
        
        if student_id in self.students:
            raise ValueError("Student already exists")
        
        student = Student(student_id, name, email)

        self.students[student_id] = student
        
        self.save_students()
        return student
    
    def delete_student(self, student_id):
        student_id = student_id.strip()
        
        if student_id not in self.students:
            raise KeyError("Student not found")
        
        student = self.students.pop(student_id)
        
        self.save_students()
        return student 
    
    def get_student(self, student_id):

        student_id = student_id.strip()

        if student_id not in self.students:
            raise KeyError("Student not found")

        return self.students[student_id]

    def list_students(self):

        return list(self.students.values())
    
    def update_student(self, student_id, name=None, email=None):

        student = self.get_student(student_id)

        student.update_profile(name, email)

        self.save_students()
        return student
