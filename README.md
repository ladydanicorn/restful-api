# Fitness Center Database Management API

A Flask-based RESTful API for managing a fitness center's member database and workout sessions. This application provides endpoints for managing member information and tracking workout sessions.

## Features

- Complete CRUD operations for member management
- Workout session scheduling and tracking
- MySQL database integration
- Error handling and appropriate HTTP status codes
- Member-specific workout session retrieval

## Prerequisites

- Python 3.x
- MySQL Server
- Virtual Environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd fitness-center-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Configure the database:
- Create a MySQL database named `fitness_center`
- Update the database configuration in `db_config.py` if needed:
  ```python
  host="localhost"
  user="fitness_app_user"
  password="codingtemple"
  database="fitness_center"
  ```

5. Run the application:
```bash
python app.py
```

## API Endpoints

### Members Management

#### Create a New Member
- **POST** `/members`
- Body:
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "membership_type": "premium"
}
```

#### Get Member by ID
- **GET** `/members/<id>`

#### Update Member
- **PUT** `/members/<id>`
- Body: Same as create member

#### Delete Member
- **DELETE** `/members/<id>`

### Workout Sessions Management

#### Schedule New Workout Session
- **POST** `/workout_sessions`
- Body:
```json
{
    "member_id": 1,
    "session_date": "2024-12-02",
    "duration": 60,
    "activity": "weight training"
}
```

#### Get Member's Workout Sessions
- **GET** `/workout_sessions/<member_id>`

## Database Schema

### Members Table
```sql
CREATE TABLE Members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    age INT NOT NULL,
    membership_type VARCHAR(50) NOT NULL
)
```

### WorkoutSessions Table
```sql
CREATE TABLE WorkoutSessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    session_date DATE NOT NULL,
    duration INT NOT NULL,
    activity VARCHAR(255) NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Members(id) ON DELETE CASCADE
)
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:
- 200: Successful operation
- 201: Resource created successfully
- 404: Resource not found
- 500: Server error

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.