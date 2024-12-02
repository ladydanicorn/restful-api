from flask import Flask
from models import create_tables
import routes

app = routes.app

if __name__ == '__main__':
    create_tables() 
    app.run(debug=True)
