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
    # table for upcoming special releases
    cursor.execute("""
    CREATE TABLE upcoming (
        special_id INT PRIMARY KEY,
        shoe_id INT NOT NULL,
        collection_name VARCHAR(31),
        release_date DATETIME,
        FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id)
    );
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
