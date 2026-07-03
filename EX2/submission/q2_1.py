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
    # creating the shoe table with id name and price
    cursor.execute("""
    CREATE TABLE shoe (
        shoe_id INT PRIMARY KEY,
        shoe_name VARCHAR(31) NOT NULL,
        price SMALLINT NOT NULL
    );
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
