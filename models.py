from db_config import get_db_connection

def create_tables():
    """Creates the Members and WorkoutSessions tables if they don't exist."""
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Members (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                age INT NOT NULL,
                membership_type VARCHAR(50) NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS WorkoutSessions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                session_date DATE NOT NULL,
                duration INT NOT NULL,
                activity VARCHAR(255) NOT NULL,
                FOREIGN KEY (member_id) REFERENCES Members(id) ON DELETE CASCADE
            )
        """)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
