import psycopg


# connect to the database
def connect():
    return psycopg.connect("dbname=A3_P1 user=postgres password=postgres")


# getting all the records in students table
def getAllStudents():
    with conn.cursor() as cursor:
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        return cursor.fetchall()


# adding a new record to students table
def addStudent(first_name, last_name, email, enrollment_date):
    with conn.cursor() as cursor:
        sql = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (first_name, last_name, email, enrollment_date))
        except Exception as e:
            print("Error: ", e)

        if cursor.rowcount > 0:
            print("Student added successfully.")
        else:
            print("Failed to add student.")


# updating a student email in students table based on student id
def updateStudentEmail(student_id, new_email):
    with conn.cursor() as cursor:
        sql = "UPDATE students SET email = %s WHERE student_id = %s"
        cursor.execute(sql, (new_email, student_id))

        if cursor.rowcount > 0:
            print("Student updated successfully.")
        else:
            print("Failed to update student.")


# deleting a student in students table based on student id
def deleteStudent(student_id):
    with conn.cursor() as cursor:
        sql = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(sql, (student_id,))

        if cursor.rowcount > 0:
            print("Student deleted successfully.")
        else:
            print("Failed to delete student.")


# printing menu and retrieving user's selection
def menu_selection():
    print("Please choose one of the following options (only the number):")
    print("\t1. Retrieving the list of all students")
    print("\t2. Adding a new student")
    print("\t3. Update a student email")
    print("\t4. Deleting a student")
    print("\t5. Quit")
    choice_str = input("Your selection: ")
    if not choice_str.isdigit() or not (1 <= int(choice_str) <= 5):
        print("Selected number should be between 1 and 5")
        return menu_selection()
    else:
        return int(choice_str)


# getting all student info from the user
def get_student_from_user():
    print("Please enter Student first name: ")
    first_name = input("")

    print("Please enter Student last name: ")
    last_name = input("")

    print("Please enter Student email: ")
    email = input("")

    print("Please enter Student enrollment_date: ")
    date = input("")

    return first_name, last_name, email, date


# getting student id and email from the user
def get_email_from_user():
    student_id = get_id_from_user()

    print("Please enter Student email: ")
    email = input("")

    return student_id, email


# getting student id from the user
def get_id_from_user():
    print("Please enter Student ID: ")
    return int(input(""))


# printing student records
def print_students(records):
    print("----------Printing all students----------")
    print(f"{'Student ID':<15}{'First Name':<15}{'Last Name':<15}{'Email':<30}{'Enrolment Date':<20}")
    for record in records:
        print(f"{record[0]:<15}{record[1]:<15}{record[2]:<15}"
              f"{record[3]:<30}{str(record[4]):<20}")


if __name__ == "__main__":
    conn = connect()
    conn.autocommit = True

    choice = 0
    while choice != 5:                  # 5: Quit
        choice = menu_selection()
        if choice == 1:
            # retrieving and printing all records
            records = getAllStudents()
            print_students(records)
        elif choice == 2:
            # inserting a new student
            first_name, last_name, email, date = get_student_from_user()
            addStudent(first_name, last_name, email, date)
        elif choice == 3:
            # updating the email of a student
            student_id, email = get_email_from_user()
            updateStudentEmail(student_id, email)
        elif choice == 4:
            # removing a student
            student_id = get_id_from_user()
            deleteStudent(student_id)
        print("-----------------------------------------")

    conn.close()







