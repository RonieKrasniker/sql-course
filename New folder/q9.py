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

    # Calculate stats per nationality: average points, min fastest lap time, and latest win date
    cursor.execute("""
    WITH AvgPoints AS (
        SELECT Nationality, AVG(PTS) AS avg_pts
        FROM drivers_updated
        GROUP BY Nationality
    ),
    MinTime AS (
        SELECT d.Nationality, MIN(f.Time) AS min_time
        FROM drivers_updated d
        JOIN fastest_laps_updated f ON d.Driver = f.Driver
        GROUP BY d.Nationality
    ),
    LatestWin AS (
        SELECT d.Nationality, MAX(w.Date) AS latest
        FROM drivers_updated d
        JOIN winners w ON d.Driver = w.Winner
        GROUP BY d.Nationality
    )
    SELECT a.Nationality, a.avg_pts, m.min_time, l.latest
    FROM AvgPoints a
    JOIN MinTime m ON a.Nationality = m.Nationality
    LEFT JOIN LatestWin l ON a.Nationality = l.Nationality
    """)
    
    print(','.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()