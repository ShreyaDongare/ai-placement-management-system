from student_manager import StudentManager
from validators import (
    validate_name,
    validate_email,
    validate_student_id
)

def main():

    manager = StudentManager()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Register Student")
        print("2. View Student")
        print("3. View All Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        try:
            choice = get_menu_choice()
            
            if choice == 1:

                student_id = validate_student_id(input("Enter Student ID: "))
                name = validate_name(input("Enter Name: "))
                email = validate_email(input("Enter Email: "))

                manager.register_student(student_id, name, email)

                print("Student registered successfully!")

            elif choice == 2:

                student_id = validate_student_id(input("Enter Student ID: "))

                student = manager.get_student(student_id)

                student.display()

            elif choice == 3:

                students = manager.list_students()

                if not students:
                    print("No students registered.")
                else:
                    for student in students:
                        print("\n----------------")
                        student.display()
                        
            elif choice == 4:

                student_id = validate_student_id(input("Enter Student ID: "))

                name_input = input("Enter New Name (leave blank to skip): ").strip()
                email_input = input("Enter New Email (leave blank to skip): ").strip()
                
                name = validate_name(name_input) if name_input else None
                email = validate_email(email_input) if email_input else None

                manager.update_student(
                    student_id,
                    name=name,
                    email=email
                )

                print("Student updated successfully!")
                
            elif choice == 5:
                student_id = validate_student_id(input("Enter Student ID: "))
                
                manager.delete_student(student_id)
                
                print("Student deleted successfully")

            elif choice == 6:

                print("Thank you!")
                break

            else:
                print("Invalid choice. Try again.")

        except (ValueError, KeyError) as error:
            print("Error:", error)

def get_menu_choice():
    choice = input("Enter your choice: ").strip()

    if not choice.isdigit():
        raise ValueError("Please enter a numeric menu choice")

    return int(choice)

if __name__ == "__main__":
    main()