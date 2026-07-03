import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2312",
        database="f1_data",
        port="3307",
    )
    cursor = mydb.cursor()

    # Query 2: Find drivers from Italy.
    # Using DISTINCT to ensure each driver appears only once.
    cursor.execute("""
    SELECT DISTINCT Driver
    FROM drivers_updated
    WHERE Nationality = 'ITA'
    """)
    
    print(','.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()