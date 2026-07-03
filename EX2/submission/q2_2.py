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
    # creating the size table for shoe sizes
    cursor.execute("""
    CREATE TABLE size (
        size_id INT PRIMARY KEY,
        european_number TINYINT NOT NULL,
        us_number TINYINT
    );
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
