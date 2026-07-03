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
    
    # Count 2001 wins for whichever team won the most in 1999
    cursor.execute("""
        SELECT COUNT(*) AS races_won
        FROM winners
        WHERE 
            YEAR(Date) = 2001
            AND Car = (
                SELECT Car
                FROM winners
                WHERE YEAR(Date) = 1999
                GROUP BY Car
                ORDER BY COUNT(*) DESC
                LIMIT 1
            )
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
