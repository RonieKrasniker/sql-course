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

    # Count wins in 2001 for the team that had the most victories in 1999
    cursor.execute("""
    SELECT COUNT(*)
    FROM winners
    WHERE YEAR(Date) = 2001 AND Car = (
        SELECT Car
        FROM winners
        WHERE YEAR(Date) = 1999
        GROUP BY Car
        ORDER BY COUNT(*) DESC
        LIMIT 1
    )
    """)
    
    print(','.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()