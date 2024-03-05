import psycopg


def connect():
    return psycopg.connect("dbname=A3_P1 user=postgres password=postgres")


def getAllStudents():
    with conn.cursor() as cursor:
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        return cursor.fetchall()


def addStudent(first_name, last_name, email, enrollment_date):
    with conn.cursor() as cursor:
        sql = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (first_name, last_name, email, enrollment_date))
        except psycopg.errors.UniqueViolation as e:
            print("Error: ", e)


def updateStudentEmail(student_id, new_email):
    with conn.cursor() as cursor:
        sql = "UPDATE students SET email = %s WHERE student_id = %s"
        cursor.execute(sql, (new_email, student_id))


def deleteStudent(student_id):
    with conn.cursor() as cursor:
        sql = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(sql, (student_id,))


if __name__ == "__main__":
    conn = connect()
    conn.autocommit = True

    # retrieving and printing all records
    records = getAllStudents()
    print("------------------Printing all students")
    for record in records:
        print(record)

    # inserting a new student
    addStudent("Charles", "Leclerc", "charles.leclerc@example.com", "1999-09-09")
    print("------------------Printing all students: adding a new student")
    for record in getAllStudents():
        print(record)

    # updating the email of a student
    updateStudentEmail(1, "john.doe@gmail.com")
    print("------------------Printing all students: updating a student")
    for record in getAllStudents():
        print(record)

    # removing a student
    deleteStudent(1)
    print("------------------Printing all students: removing a student")
    for record in getAllStudents():
        print(record)