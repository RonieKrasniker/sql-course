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

    # Query 1: Find drivers from Brazil.
    # Using DISTINCT to remove duplicate driver names.
    cursor.execute("""
    SELECT DISTINCT Driver
    FROM drivers_updated
    WHERE Nationality = 'BRA'
    """)
    
    print(','.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()