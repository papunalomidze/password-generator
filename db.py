import mysql.connector
from mysql.connector import Error

def create_table():
    try:
        conn = mysql.connector.connect(
            host='papuna.mysql.pythonanywhere-services.com',
            user='papuna',
            password='qwe123123',
            database='papuna$users'
        )

        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """

        cursor.execute(create_table_query)
        conn.commit()

        print("Table created successfully")

    except Error as e:
        print(e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    create_table()
