import mysql.connector

def create_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",  # Assuming 'root' as per example, user should change if needed
            port='3307'
        )
        cursor = mydb.cursor()
        
        # Create Database
        cursor.execute("DROP DATABASE IF EXISTS Hosppdd")
        cursor.execute("CREATE DATABASE Hosppdd")
        cursor.execute("USE Hosppdd")
        
        # 1. Hospital Table
        cursor.execute("""
        CREATE TABLE Hospital (
            hid INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """)
        
        # 2. Medicine Table
        cursor.execute("""
        CREATE TABLE Medicine (
            mid INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """)
        
        # 3. Disease Table
        cursor.execute("""
        CREATE TABLE Disease (
            kid INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            severity VARCHAR(50),
            medicine_id INT NOT NULL,
            FOREIGN KEY (medicine_id) REFERENCES Medicine(mid)
        )
        """)
        
        # 4. Doctor Table
        # Note: 'consultant' is a recursive relationship. 
        # Doctor ID is unique per Hospital, so PK is (hid, did).
        cursor.execute("""
        CREATE TABLE Doctor (
            hid INT,
            did INT,
            name VARCHAR(255) NOT NULL,
            consultant_hid INT,
            consultant_did INT,
            PRIMARY KEY (hid, did),
            FOREIGN KEY (hid) REFERENCES Hospital(hid),
            FOREIGN KEY (consultant_hid, consultant_did) REFERENCES Doctor(hid, did)
        )
        """)
        
        # 5. Patient Table
        # 'treating_doctor' -> (hid, did)
        # 'new_disease' -> kid
        # 'prev_disease' -> kid (nullable)
        cursor.execute("""
        CREATE TABLE Patient (
            pid INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            height FLOAT,
            weight FLOAT,
            gender VARCHAR(10),
            treating_hid INT NOT NULL,
            treating_did INT NOT NULL,
            new_disease_id INT NOT NULL,
            prev_disease_id INT,
            FOREIGN KEY (treating_hid, treating_did) REFERENCES Doctor(hid, did),
            FOREIGN KEY (new_disease_id) REFERENCES Disease(kid),
            FOREIGN KEY (prev_disease_id) REFERENCES Disease(kid)
        )
        """)
        
        # 6. Rating Table
        # Patient rates Doctor.
        # Assuming one rating per patient-doctor interaction, or just one per patient?
        # Prompt: "Each patient is asked to rate the doctor who took care of him."
        # Prompt: "The basic rating contains a unique rating id and a rating."
        cursor.execute("""
        CREATE TABLE Rating (
            rid INT PRIMARY KEY,
            score INT NOT NULL,
            pid INT NOT NULL,
            rated_hid INT NOT NULL,
            rated_did INT NOT NULL,
            FOREIGN KEY (pid) REFERENCES Patient(pid),
            FOREIGN KEY (rated_hid, rated_did) REFERENCES Doctor(hid, did)
        )
        """)
        
        # 7. Opinion Table (Enhanced Rating)
        # Inheritance from Rating
        cursor.execute("""
        CREATE TABLE Opinion (
            rid INT PRIMARY KEY,
            comment TEXT,
            FOREIGN KEY (rid) REFERENCES Rating(rid) ON DELETE CASCADE
        )
        """)

        # Commit logic
        mydb.commit()
        cursor.close()
        mydb.close()
        print("Database Hosppdd and tables created successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == '__main__':
    create_database()
