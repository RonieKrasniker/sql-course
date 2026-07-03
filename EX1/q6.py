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
    
    # Find Grand Prix pairs with same lap count (80 or more)
    # Using w1 < w2 to avoid duplicate pairs like (A,B) and (B,A)
    cursor.execute("""
        SELECT 
            w1.`Grand Prix` AS GP1,
            w2.`Grand Prix` AS GP2,
            w1.Laps
        FROM winners AS w1
        INNER JOIN winners AS w2 
            ON w1.Laps = w2.Laps 
            AND w1.`Grand Prix` < w2.`Grand Prix`
        WHERE 
            w1.Laps >= 80
            AND w1.Laps IS NOT NULL
        GROUP BY w1.`Grand Prix`, w2.`Grand Prix`, w1.Laps
        ORDER BY GP1, GP2
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
