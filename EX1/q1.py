import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port="3307",
    )
    cursor = mydb.cursor()
    
    # Get all Brazilian drivers (no duplicates)
    cursor.execute("""
        SELECT DISTINCT Driver
        FROM drivers_updated
        WHERE Nationality = 'BRA'
        ORDER BY Driver ASC
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
