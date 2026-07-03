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
    
    # Find the 2000 winner with most laps and their best time
    # First get who had the most total laps in 2000, then find their fastest time
    cursor.execute("""
        SELECT 
            w.Winner AS Driver,
            MIN(f.Time) AS min_time
        FROM winners AS w
        INNER JOIN fastest_laps_updated AS f 
            ON w.`Name Code` = f.Code AND YEAR(w.Date) = f.year
        WHERE 
            YEAR(w.Date) = 2000
            AND w.Winner = (
                SELECT Winner
                FROM winners
                WHERE YEAR(Date) = 2000 AND Laps IS NOT NULL
                GROUP BY Winner
                ORDER BY SUM(Laps) DESC
                LIMIT 1
            )
        GROUP BY w.Winner
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
