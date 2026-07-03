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
    # inserting orders
    cursor.execute("""
    INSERT INTO company_order (order_id, order_date) VALUES
    (1, '2025-01-15 14:30:00'), (2, '2025-02-10 10:15:00'), (3, '2025-03-05 16:45:00'),
    (4, '2025-04-12 09:00:00'), (5, '2025-05-20 11:00:00'), (6, '2025-06-01 13:30:00'),
    (7, '2025-07-10 15:45:00'), (8, '2025-08-15 17:00:00'), (9, '2025-09-05 19:30:00'),
    (10, '2025-10-22 08:15:00'), (11, '2025-11-01 12:30:00'), (12, '2025-12-10 14:45:00'),
    (13, '2025-02-18 10:00:00'), (14, '2025-03-20 08:15:00'), (15, '2025-04-22 16:30:00');
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
