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
    # table for countries we operate in
    cursor.execute("""
    CREATE TABLE country (
        country_id INT PRIMARY KEY,
        country_name VARCHAR(63) NOT NULL
    );
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
