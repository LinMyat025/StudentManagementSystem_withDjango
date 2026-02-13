# Student Management System 🎓

A simple, beginner-friendly Web Application built with Python and Django to manage student records. This project demonstrates full CRUD (Create, Read, Update, Delete) operations connected to a PostgreSQL backend database.

🌟 Features
Create: Add new students to the database with their Name, Email, Gender, and Phone number.

Read: View a formatted, responsive table of all registered students on the homepage.

Update: Edit existing student details with forms that automatically pre-fill with their current data.

Delete: Remove a student from the database, featuring a JavaScript confirmation popup to prevent accidental deletions.

🛠️ Technologies Used
Backend: Python, Django

Database: PostgreSQL

Frontend: HTML5, CSS3, Bootstrap 5 (CDN)

Environment: Virtual Environment (venv), requirements.txt

📂 Folder Structure
APP/ - The main Django application handling the views, URLs, and database models.

StudentManagement/ - The core Django configuration folder (contains settings.py).

static/ - Contains custom CSS files (createEditStyle.css) for styling the frontend.

templates/ - Contains the HTML files (index.html, create.html, edit.html).

manage.py - The Django command-line utility for administrative tasks.

🚀 How to Run This Project Locally
If you want to download and run this project on your own computer, follow these exact steps:

1. Prerequisites
You must have the following installed on your machine:

Python

PostgreSQL

2. Set up the Database
Open pgAdmin (or your PostgreSQL SQL Shell) and create a new, empty database:

SQL
CREATE DATABASE student_db;
3. Clone or Download the Repository
Download this code to your local machine and open the project folder in your terminal (like VS Code or Command Prompt).

4. Create a Virtual Environment & Install Requirements
It is highly recommended to run this in a virtual environment.

Bash
# Create the virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt
5. Update Database Settings
Open the StudentManagement/settings.py file. Scroll down to the DATABASES section and update the 'PASSWORD' field with your own PostgreSQL password:

Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'student_db',
        'USER': 'postgres',
        'PASSWORD': 'YOUR_PASSWORD_HERE',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
6. Run Migrations
Generate the database tables in PostgreSQL by running:

Bash
python manage.py makemigrations
python manage.py migrate
7. Start the Server
Run the local development server:

Bash
python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/ to use the app!
