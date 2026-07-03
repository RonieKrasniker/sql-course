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

    # List drivers who drove for Ferrari OR are from Argentina
    cursor.execute("""
    SELECT DISTINCT Driver
    FROM drivers_updated
    WHERE Driver IN (SELECT Winner FROM winners WHERE Car = 'Ferrari') 
       OR Nationality = 'ARG'
    ORDER BY Driver ASC
    """)
    
    print(','.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()