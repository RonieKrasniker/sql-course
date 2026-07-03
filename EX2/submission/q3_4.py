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
    # inserting upcoming releases
    cursor.execute("""
    INSERT INTO upcoming (special_id, shoe_id, collection_name, release_date) VALUES
    (1, 1, 'Air Max Day 2025', '2025-03-26 10:00:00'),
    (2, 1, 'Spring Breeze Collection', '2025-05-15 12:00:00'),
    (3, 2, 'Yeezy Glow Pack', '2025-06-15 09:00:00'),
    (4, 2, 'Summer Neon Edition', '2025-08-10 11:00:00'),
    (5, 4, 'Jordan Anniversary', '2025-08-22 12:00:00'),
    (6, 4, 'Jordan Lunar Collection', '2025-10-05 14:00:00'),
    (7, 6, 'Lunar Bright Collection', '2025-09-30 08:00:00'),
    (8, 7, 'HyperFlux Supreme', '2025-10-10 15:00:00'),
    (9, 9, 'Quantum Special Edition', '2025-11-05 18:00:00'),
    (10, 9, 'Winter Starlight Pack', '2025-12-20 20:00:00'),
    (11, 10, 'Echo Runner Series', '2025-01-18 09:00:00'),
    (12, 10, 'Trail Explorer Edition', '2025-07-25 17:00:00');
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
