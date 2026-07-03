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
    # calculating total revenue per customer
    cursor.execute("""
    SELECT c.first_name, c.last_name, SUM(s.price) as total_spent
    FROM customer c
    JOIN order_customer oc ON c.customer_id = oc.customer_id
    JOIN company_order co ON oc.order_id = co.order_id
    JOIN order_shoe os ON co.order_id = os.order_id
    JOIN shoe s ON os.shoe_id = s.shoe_id
    GROUP BY c.customer_id, c.first_name, c.last_name;
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    
    cursor.close()
    mydb.close()
