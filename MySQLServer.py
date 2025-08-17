import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server and create database
        conn = mysql.connector.connect(
            host='localhost',
            user='fakor',
            password='p@ssw0rd'
        )
        cursor = conn.cursor()


        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to create database: {err}")
        finally:

            cursor.close()
            conn.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Incorrect username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")

if __name__ == "__main__":
    create_database()
