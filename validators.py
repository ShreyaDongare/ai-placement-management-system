def validate_name(name):
    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty")

    return name


def validate_email(email):
    email = email.strip()

    if not email:
        raise ValueError("Email cannot be empty")

    if "@" not in email:
        raise ValueError("Enter a valid email address")

    return email

def validate_student_id(student_id):
    student_id = student_id.strip()

    if not student_id:
        raise ValueError("Student ID cannot be empty")

    return student_id