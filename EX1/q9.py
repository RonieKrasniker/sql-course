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
    
    # Stats by nationality: avg points, fastest time, most recent win
    # Using 3 WITH clauses to calculate each stat separately then join them
    cursor.execute("""
        WITH avg_points AS (
            SELECT 
                Nationality,
                AVG(PTS) AS avg_pts
            FROM drivers_updated
            GROUP BY Nationality
        ),
        min_fastest AS (
            SELECT 
                d.Nationality,
                MIN(f.Time) AS min_time
            FROM drivers_updated AS d
            INNER JOIN fastest_laps_updated AS f 
                ON d.Code = f.Code AND d.year = f.year
            WHERE f.Time IS NOT NULL
            GROUP BY d.Nationality
        ),
        latest_win AS (
            SELECT 
                d.Nationality,
                MAX(w.Date) AS latest
            FROM drivers_updated AS d
            INNER JOIN winners AS w 
                ON d.Code = w.`Name Code` AND d.year = YEAR(w.Date)
            WHERE w.Date IS NOT NULL
            GROUP BY d.Nationality
        )
        SELECT 
            ap.Nationality,
            ap.avg_pts,
            mf.min_time,
            lw.latest
        FROM avg_points AS ap
        LEFT JOIN min_fastest AS mf ON ap.Nationality = mf.Nationality
        LEFT JOIN latest_win AS lw ON ap.Nationality = lw.Nationality
        ORDER BY ap.Nationality ASC
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
