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

    # Find the driver who won in 2000 with the most laps
    # Return driver name and their best time
    cursor.execute("""
    SELECT w.Winner, MIN(f.Time)
    FROM winners w
    JOIN fastest_laps_updated f ON w.Winner = f.Driver
    WHERE YEAR(w.Date) = 2000 AND f.year = 2000
    GROUP BY w.Winner
    ORDER BY SUM(w.Laps) DESC
    LIMIT 1
    """)
    
    print(','.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()