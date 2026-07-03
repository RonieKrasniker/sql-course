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
    # mapping shoes to sizes
    cursor.execute("""
    INSERT INTO shoe_size (shoe_id, size_id) VALUES
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
    (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10),
    (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
    (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10),
    (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12);
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
