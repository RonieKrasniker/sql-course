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
    
    # Drivers who either won for Ferrari OR are from Argentina
    # UNION combines both groups without duplicates
    cursor.execute("""
        SELECT DISTINCT d.Driver AS driver
        FROM drivers_updated AS d
        INNER JOIN winners AS w 
            ON d.Code = w.`Name Code` AND d.year = YEAR(w.Date)
        WHERE w.Car = 'Ferrari'
        
        UNION
        
        SELECT DISTINCT Driver AS driver
        FROM drivers_updated
        WHERE Nationality = 'ARG'
        
        ORDER BY driver ASC
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
