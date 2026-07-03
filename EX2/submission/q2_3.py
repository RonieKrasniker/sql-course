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
    # connecting shoes to their available sizes
    cursor.execute("""
    CREATE TABLE shoe_size (
        shoe_id INT,
        size_id INT,
        PRIMARY KEY (shoe_id, size_id),
        FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id),
        FOREIGN KEY (size_id) REFERENCES size(size_id)
    );
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
