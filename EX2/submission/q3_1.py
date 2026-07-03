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
    # inserting the shoes data
    cursor.execute("""
    INSERT INTO shoe (shoe_id, shoe_name, price) VALUES
    (1, 'Air CS 0/1', 150), (2, 'Yeezy Gauss 360', 220), (3, '1B All Star', 60),
    (4, 'Jordan 1 Engineering', 170), (5, 'BIU Superstar', 90), (6, 'Lunar Glow', 200),
    (7, 'HyperFlux', 180), (8, 'Nebula Runner', 140), (9, 'Quantum Charge', 250),
    (10, 'Echo Boost', 160), (11, 'Storm Runner', 130), (12, 'Apex Boost', 190),
    (13, 'Velocity Wave', 170), (14, 'Stride Master', 100), (15, 'Trail Blazer', 200),
    (16, 'Infinity Glide', 180), (17, 'Solar Charge', 150), (18, 'Pace Leader', 120),
    (19, 'Canyon Racer', 250), (20, 'Sky High', 210);
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
