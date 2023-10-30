import mysql.connector 

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database = "school1"
    )

def create_database(db_name):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def create_table(db_name, table_name, fields):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(f"USE {db_name}")
        create_table_query = f"CREATE TABLE {table_name} ({fields})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created or already exists in '{db_name}' database.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def insert_record(db_name, table_name, values):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(f"USE {db_name}")
        insert_query = f"INSERT INTO {table_name} VALUES {values}"
        cursor.execute(insert_query)
        conn.commit()
        print("Record inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def view_records(db_name, table_name):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        for record in records:
            print(record)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    create_database("student")
    create_database("marks")
    create_database("subjects")

    create_table("student", "student_details", "sl_no INT AUTO_INCREMENT PRIMARY KEY, id VARCHAR(30), name VARCHAR(255), lname VARCHAR(255), phone_no VARCHAR(15)")
    create_table("marks", "marks_details", "id INT, phy INT, chem INT, maths INT, eng INT")
    create_table("subjects", "subjects_details", "subject_id INT AUTO_INCREMENT PRIMARY KEY, subject_name VARCHAR(255")

    while True:
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            table_name = input("Enter table name: ")
            values = input("Enter record values (e.g., (value1, value2, ...)): ")
            insert_record("student", table_name, values)

        elif choice == "2":
            table_name = input("Enter table name: ")
            view_records("student", table_name)

        elif choice == "3":
            break
