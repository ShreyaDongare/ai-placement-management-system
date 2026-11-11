from student_manager import StudentManager

def main():

    manager = StudentManager()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Register Student")
        print("2. View Student")
        print("3. View All Students")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        
        try:
            
            if choice == "1":

                student_id = input("Enter Student ID: ")
                name = input("Enter Name: ")
                email = input("Enter Email: ")

                manager.register_student(student_id, name, email)

                print("Student registered successfully!")

            elif choice == "2":

                student_id = input("Enter Student ID: ")

                student = manager.get_student(student_id)

                student.display()

            elif choice == "3":

                students = manager.list_students()

                if not students:
                    print("No students registered.")
                else:
                    for student in students:
                        print("\n----------------")
                        student.display()
                        
            elif choice == "4":

                student_id = input("Enter Student ID: ")

                name = input("Enter New Name (leave blank to skip): ")
                email = input("Enter New Email (leave blank to skip): ")

                manager.update_student(
                    student_id,
                    name=name or None,
                    email=email or None
                )

                print("Student updated successfully!")

            elif choice == "5":

                print("Thank you!")
                break

            else:
                print("Invalid choice. Try again.")

        except (ValueError, KeyError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()