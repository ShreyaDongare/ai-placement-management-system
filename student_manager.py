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
        
class StudentManager:

    def __init__(self):
        self.students = {}
        
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

        return student
