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
    # linking orders to shoes
    cursor.execute("""
    CREATE TABLE order_shoe (
        order_id INT,
        shoe_id INT,
        PRIMARY KEY (order_id, shoe_id),
        FOREIGN KEY (order_id) REFERENCES company_order(order_id),
        FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id)
    );
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
