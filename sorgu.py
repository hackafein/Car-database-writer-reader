import sqlite3

def verial(users):
    try:
        sqliteConnection = sqlite3.connect('askfm.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from sorucevap where Users = ? """
        cursor.execute(sql_select_query, (users,))
        records = cursor.fetchall()
        

        for row in records:
            print(" Users = ", row[0])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

