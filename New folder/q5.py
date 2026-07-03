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

    # Compute average points per car for cars with fastest lap time below 2 minutes
    cursor.execute("""
    SELECT t.Car, AVG(t.PTS) AS avg_pts
    FROM teams_updated t
    JOIN fastest_laps_updated f ON t.Car = f.Car
    WHERE MINUTE(STR_TO_DATE(f.Time, '%i:%s.%f')) < 2
    GROUP BY t.Car
    ORDER BY avg_pts DESC
    """)
    
    print(','.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()