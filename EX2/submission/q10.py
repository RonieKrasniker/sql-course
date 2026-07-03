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
    # combining inventory and upcoming releases
    cursor.execute("""
    SELECT shoe_name as name, 'Inventory' as source FROM shoe
    UNION
    SELECT collection_name as name, 'Upcoming Release' as source FROM upcoming;
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    
    cursor.close()
    mydb.close()
