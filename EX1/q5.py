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
    
    # Average points by car - only for cars with fastest laps under 2 minutes
    # Need to join on both car name and year to match correctly
    cursor.execute("""
        SELECT 
            t.Car,
            AVG(t.PTS) AS avg_pts
        FROM teams_updated AS t
        INNER JOIN fastest_laps_updated AS f 
            ON t.Car = f.Car AND t.year = f.year
        WHERE 
            f.Time IS NOT NULL
            AND MINUTE(STR_TO_DATE(f.Time, '%i:%s.%f')) < 2
        GROUP BY t.Car
        ORDER BY avg_pts DESC
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
