from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Database configuration using environment variables
db_user = os.environ.get('DB_USER', 'benasblaskevicius')
db_password = os.environ.get('DB_PASSWORD', 'yourdefaultdbpassword')
db_name = os.environ.get('DB_NAME', 'benasblaskevicius')
db_host = os.environ.get('DB_HOST', 'localhost')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Import models (after db variable initialization)
from . import models

@app.route('/')
def home():
    return render_template('index.html')

# Add additional routes here
migrate = Migrate(app, db)

# Run this if you're not using Flask's CLI to run the application
if __name__ == '__main__':
    app.run(debug=True)
