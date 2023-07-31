from config import db_connection


class Student:
    def list_student_info(self):
        try:
            # DB connection
            connection = db_connection()
            curser = connection.cursor()

            query = '''
              SELECT * FROM student
            '''
            curser.execute(query)
            print('All Students: \n')
            students = curser.fetchall()
            for student in students:
                print('Id: ', student[0],'\n')
                print('Name: ', student[1],'\n')
                print('Class: ', student[2],'\n')
                print('Roll no: ', student[3])
                print('\n---------------------------------\n')

            print('Total Students:', len(students))

            connection.commit()

        except Exception as e:
            print(str(e))

    def add_student_info(self):
        student_name = input('Enter Student Name: ')
        student_class = input('Enter Student Class: ')
        studnet_roll_no = input('Enter Student Rollno: ')

        try:
            # DB connection
            connection = db_connection()
            curser = connection.cursor()

            add_query = '''
                INSERT INTO student (name,class,rollno) 
                VALUES (%s,%s,%s) 
            '''
            data = (student_name, student_class, studnet_roll_no)
            curser.execute(add_query, data)

            query = '''
              SELECT * FROM student
            '''
            curser.execute(query)
            print('\nNew Student is added:\n')

            students = curser.fetchall()
            for student in students:
                print('Id: ', student[0],'\n')
                print('Name: ', student[1],'\n')
                print('Class: ', student[2],'\n')
                print('Roll no: ', student[3])
                print('\n---------------------------------\n')

            print('Total Students:', len(students))

            connection.commit()

        except Exception as e:
            print(str(e))

    def edit_student_info(self):
        print('Which Student you want to udpate?\n')
        student_name = input('Enter Student Name: ')
        student_class = input('Enter Student Class: ')
        studnet_roll_no = input('Enter Student Rollno: ')
        try:
            connection = db_connection()
            curser = connection.cursor()

            edit_query = '''
                UPDATE student set class = %s, rollno = %s where name = %s
             '''
            data = (student_class, studnet_roll_no, student_name)
            curser.execute(edit_query, data)

            query = '''
              SELECT * FROM student
            '''
            curser.execute(query)
            print('\nNew Student is added:\n')

            students = curser.fetchall()
            for student in students:
                print('Id: ', student[0],'\n')
                print('Name: ', student[1],'\n')
                print('Class: ', student[2],'\n')
                print('Roll no: ', student[3])
                print('\n---------------------------------\n')

            print('Total Students:', len(students))

            connection.commit()

        except Exception as e:
            print(e)

    def delete_student(self):
        id = input('Enter the id of student you want to delete:')

        try: 
            connection = db_connection()
            curser = connection.cursor()

            delete_query = '''
                DELETE from student where id=%s
             '''
            data = (id)
            curser.execute(delete_query, data)

            query = '''
              SELECT * FROM student
            '''
            curser.execute(query)

            print('\nUpdated Student Table:\n')

            students = curser.fetchall()
            for student in students:
                print('Id: ', student[0],'\n')
                print('Name: ', student[1],'\n')
                print('Class: ', student[2],'\n')
                print('Roll no: ', student[3])
                print('\n---------------------------------\n')
            print('Total Students:', len(students))
            connection.commit()
        
        except Exception as e:
            print(e)
