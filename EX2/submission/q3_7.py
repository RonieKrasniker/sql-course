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
    # inserting customer details
    cursor.execute("""
    INSERT INTO customer (customer_id, first_name, last_name, email, city_id) VALUES
    ('123456789', 'John', 'Doe', 'john.doe@example.com', 1),
    ('987654321', 'Jane', 'Smith', 'jane.smith@example.com', 2),
    ('112233445', 'Alice', 'Brown', 'alice.brown@example.com', 3),
    ('223344556', 'Bob', 'White', 'bob.white@example.com', 4),
    ('334455667', 'Eve', 'Green', 'eve.green@example.com', 5),
    ('445566778', 'Chris', 'Black', 'chris.black@example.com', 6),
    ('556677889', 'Anna', 'Taylor', 'anna.taylor@example.com', 7),
    ('667788990', 'Max', 'Johnson', 'max.johnson@example.com', 8),
    ('778899001', 'Lily', 'Adams', 'lily.adams@example.com', 9),
    ('889900112', 'Oscar', 'Hill', 'oscar.hill@example.com', 10);
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
