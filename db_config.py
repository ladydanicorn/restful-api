import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="fitness_app_user",
        password="codingtemple",
        database="fitness_center",
    )

if __name__ == "__main__":
    try:
        connection = get_db_connection()
        print("Database connection successful")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals():
            connection.close()
