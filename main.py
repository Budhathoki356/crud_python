from student import Student

def main():
    student = Student()

    option = input('''
        Provide the number:\n
        1. List Students
        2. Add Student
        3. Edit Student
        4. Delete Student
    ''')

    if option == '1':
        student.list_student_info()
    elif option == '2':
        student.add_student_info()
    elif option == '3':
        student.edit_student_info()
    elif option == '4':
        student.delete_student()
    
# Starting App
main()
