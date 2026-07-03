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

    # Find pairs of different Grand Prix events with the same number of laps (>80)
    # The condition GP1 < GP2 ensures alphabetical order and no duplicates
    cursor.execute("""
    SELECT w1.`Grand Prix` AS GP1, w2.`Grand Prix` AS GP2, w1.Laps
    FROM winners w1
    JOIN winners w2 ON w1.Laps = w2.Laps
    WHERE w1.Laps >= 80 
      AND w1.`Grand Prix` < w2.`Grand Prix`
    GROUP BY w1.`Grand Prix`, w2.`Grand Prix`, w1.Laps
    """)
    
    print(','.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()