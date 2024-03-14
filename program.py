import psycopg2
import os
from psycopg2 import sql

# Function to retrieve the database credentials stored as environment variables
def get_database_credentials():
    dbname = os.environ.get('DB_NAME')
    user = os.environ.get('user')
    password = os.environ.get('password')
    host = os.environ.get('host')
    port = os.environ.get('port')
    return dbname, user, password, host, port

# Function to check if the student table is already populated
def checkIfPopulated():
    cur.execute("SELECT COUNT(*) FROM students")
    # Fetch the result
    row_count = cur.fetchone()[0]
    if(row_count == 0):
        return False
    else:
        return True

# Establish a connection to the database
dbname, user, password, host, port = get_database_credentials()
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)
# Establish cursor
cur = conn.cursor()
    
# Question 1:
def getAllStudents():
    # SQL Query
    query = """SELECT * FROM students"""

    # Execute the SQL 
    cur.execute(query)

    # Retrieve the returned rows from the query
    rows = cur.fetchall()

    #Print all the rows in the console
    for row in rows:
        print("Student ID:", row[0])
        print("First Name:", row[1])
        print("Last Name:", row[2])
        print("Email:", row[3])
        print("Enrollment Date:", row[4])
        print("\n")

# Question 2:
def addStudent(first_name, last_name, email, enrollment_date):

    # SQL Query
    query = """INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s)"""
    
    # Execute the SQL and commit the changes to the database
    cur.execute(query, (first_name,last_name,email,enrollment_date))
    conn.commit()

# Question 3:
def updateStudentEmail(student_id, new_email):

    #SQL Query
    query = """
        UPDATE students
        SET email = %s
        WHERE student_id = %s    
    """

    # Execute the SQL and commit the changes to the database
    cur.execute(query, (new_email,student_id))
    conn.commit()

# Question 4
def deleteStudent(student_id):

    #SQL Query
    query = """
        DELETE FROM students
        WHERE student_id = %s
    """

     # Execute the SQL and commit the changes to the database
    cur.execute(query, (student_id,))
    conn.commit()

# Function to populate initial data from specs
def initPopulate():
    create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            enrollment_date DATE
        )
    """
    cur.execute(create_table_query)

    init_insert = """INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');"""

    if not checkIfPopulated():
        cur.execute(init_insert)


    conn.commit()
# Call to populate the table with the given data
initPopulate()

# Loop that prompts the user to execute the required questions
while True:
    choice = int(input("1. Question 1 test getAllStudents()\n2. Question 2 test addStudent()\n3. Question 3 test updateStudentEmail()\n4. Question 4 test deleteStudent()\n5. quit\nWhich option would you like to test: "))
    match choice:
        case 1:
            getAllStudents()
        case 2:
            string_vals = input("Enter first_name, last_name, email, enrollment_date in that order separated by spaces:")
            values = string_vals.split()
            addStudent(values[0],values[1],values[2],values[3])
        case 3:
            string_vals = input("Enter student_id, new_email in that order separated by spaces:")
            values = string_vals.split()
            updateStudentEmail(int(values[0]),values[1])
        case 4:
            val = int(input("Enter student_id "))
            deleteStudent(val)
        case 5:
            break;

# Close the cursor and connection to the database
cur.close()
conn.close()