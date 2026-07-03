import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="root",
    database="f1_data", port="3307"
)
cursor = mydb.cursor()

# Check: How many Ferrari records in teams_updated?
cursor.execute("SELECT COUNT(*) FROM teams_updated WHERE Car = 'Ferrari'")
print(f"Ferrari in teams_updated: {cursor.fetchone()[0]}")

# Check: How many Ferrari fastest laps?
cursor.execute("SELECT COUNT(*) FROM fastest_laps_updated WHERE Car = 'Ferrari'")
print(f"Ferrari in fastest_laps: {cursor.fetchone()[0]}")

# Check with year join
cursor.execute(""
SELECT COUNT(*) 
FROM teams_updated t
JOIN fastest_laps_updated f ON t.Car = f.Car AND t.year = f.year
WHERE t.Car = 'Ferrari' AND MINUTE(STR_TO_DATE(f.Time, '%i:%s.%f')) < 2
"")
print(f"Ferrari rows with year join: {cursor.fetchone()[0]}")

# Check without year join  
cursor.execute(""
SELECT COUNT(*)
FROM teams_updated t
JOIN fastest_laps_updated f ON t.Car = f.Car
WHERE t.Car = 'Ferrari' AND MINUTE(STR_TO_DATE(f.Time, '%i:%s.%f')) < 2
"")
print(f"Ferrari rows without year join: {cursor.fetchone()[0]}")

cursor.close()
mydb.close()
