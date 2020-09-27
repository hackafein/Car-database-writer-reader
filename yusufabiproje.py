import sqlite3

try:
    sqliteConnection = sqlite3.connect('urun.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO uruntablo
                          (Kodu, Tipi,Volt , Boy, Çap, Diş, Araçlar) 
                           VALUES 
                          (123123,'James','12','20','80','2','fiat')"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into urun table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
