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

    # Calculate the points difference between Ferrari and Maserati
    cursor.execute("""
    SELECT 
        (SELECT SUM(PTS) FROM teams_updated WHERE Car = 'Ferrari') -
        (SELECT SUM(PTS) FROM teams_updated WHERE Car = 'Maserati') AS diff
    """)
    
    print(','.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()