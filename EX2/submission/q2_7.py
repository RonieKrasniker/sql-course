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
    # customer details with check for id length
    cursor.execute("""
    CREATE TABLE customer (
        customer_id VARCHAR(15) PRIMARY KEY,
        first_name VARCHAR(31) NOT NULL,
        last_name VARCHAR(31) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        city_id INT NOT NULL,
        CHECK (LENGTH(customer_id) = 9),
        FOREIGN KEY (city_id) REFERENCES city(city_id)
    );
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
