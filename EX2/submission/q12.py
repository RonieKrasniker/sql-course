import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port='3307',
    )
    
    cursor = mydb.cursor()
    # finding shoes that haven't been ordered
    cursor.execute("""
    SELECT DISTINCT s.shoe_name
    FROM shoe s
    LEFT JOIN order_shoe os ON s.shoe_id = os.shoe_id
    WHERE os.order_id IS NULL;
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    
    cursor.close()
    mydb.close()
