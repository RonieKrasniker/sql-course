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
    # table for cities linked to countries
    cursor.execute("""
    CREATE TABLE city (
        city_id INT PRIMARY KEY,
        city_name VARCHAR(63) NOT NULL,
        country_id INT NOT NULL,
        FOREIGN KEY (country_id) REFERENCES country(country_id)
    );
    """)
    
    #!!! Commit the transaction to save the changes to the database!!!
    mydb.commit()
    
    cursor.close()
    mydb.close()
