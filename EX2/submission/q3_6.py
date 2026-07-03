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
    # inserting cities
    cursor.execute("""
    INSERT INTO city (city_id, city_name, country_id) VALUES
    (1, 'Jerusalem', 1), (2, 'Tel Aviv', 1), (3, 'Haifa', 1),
    (4, 'Toronto', 2), (5, 'Vancouver', 2), (6, 'Montreal', 2),
    (7, 'Los Angeles', 3), (8, 'New York', 3), (9, 'Chicago', 3), (10, 'Houston', 3),
    (11, 'Berlin', 4), (12, 'Munich', 4), (13, 'Frankfurt', 4), (14, 'Hamburg', 4),
    (15, 'Paris', 5), (16, 'Lyon', 5), (17, 'Marseille', 5),
    (18, 'Tokyo', 6), (19, 'Osaka', 6), (20, 'Kyoto', 6),
    (21, 'Sydney', 7), (22, 'Melbourne', 7), (23, 'Brisbane', 7),
    (24, 'Rome', 8), (25, 'Milan', 8), (26, 'Naples', 8),
    (27, 'Madrid', 9), (28, 'Barcelona', 9), (29, 'Seville', 9),
    (30, 'Rio de Janeiro', 10), (31, 'São Paulo', 10), (32, 'Brasilia', 10);
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
