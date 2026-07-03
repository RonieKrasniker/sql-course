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
    # calculating average price per size
    cursor.execute("""
    SELECT sz.european_number, sz.us_number, AVG(s.price) as avg_price
    FROM size sz
    JOIN shoe_size ss ON sz.size_id = ss.size_id
    JOIN shoe s ON ss.shoe_id = s.shoe_id
    GROUP BY sz.size_id, sz.european_number, sz.us_number
    ORDER BY avg_price DESC;
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    
    cursor.close()
    mydb.close()
