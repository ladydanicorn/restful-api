from flask import Flask, request, jsonify
from db_config import get_db_connection

app = Flask(__name__)

@app.route('/members', methods=['POST'])
def add_member():
    """Adds a new member."""
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO Members (name, email, age, membership_type) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['name'], data['email'], data['age'], data['membership_type']))
        connection.commit()
        return jsonify({"message": "Member added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    """Retrieves a member by ID."""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(query, (id,))
        member = cursor.fetchone()
        if not member:
            return jsonify({"error": "Member not found"}), 404
        return jsonify(member), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    """Updates an existing member."""
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "UPDATE Members SET name = %s, email = %s, age = %s, membership_type = %s WHERE id = %s"
        cursor.execute(query, (data['name'], data['email'], data['age'], data['membership_type'], id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Member not found"}), 404
        return jsonify({"message": "Member updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    """Deletes a member."""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "DELETE FROM Members WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Member not found"}), 404
        return jsonify({"message": "Member deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/workout_sessions', methods=['POST'])
def add_workout_session():
    """Schedules a new workout session."""
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO WorkoutSessions (member_id, session_date, duration, activity) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['member_id'], data['session_date'], data['duration'], data['activity']))
        connection.commit()
        return jsonify({"message": "Workout session added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/workout_sessions/<int:member_id>', methods=['GET'])
def get_workout_sessions_for_member(member_id):
    """Retrieves all workout sessions for a specific member."""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM WorkoutSessions WHERE member_id = %s"
        cursor.execute(query, (member_id,))
        sessions = cursor.fetchall()
        if not sessions:
            return jsonify({"error": "No workout sessions found for this member"}), 404
        return jsonify(sessions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()
