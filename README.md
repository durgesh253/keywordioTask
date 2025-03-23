# Library Management System

A Django-based Library Management System that allows administrators to manage book inventory and provides a simple interface for students to view books.

## Features

- Admin authentication (signup/login)
- Book management (CRUD operations)
- Student view to browse available books
- RESTful API for integration with other systems

## Technologies Used

- Django 4.2
- Django REST Framework
- MySQL Database
- Bootstrap 5 (for UI)

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL Server

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd library-project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the MySQL database in `library_project/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'library_management',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. Create the MySQL database:
   ```sql
   CREATE DATABASE library_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

6. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```bash
   python manage.py runserver
   ```

9. Access the application at http://127.0.0.1:8000/

## Project Structure

```
library_management_system/
├── library_project/       # Main project settings
├── library_app/           # Main application
│   ├── models.py          # Data models
│   ├── serializers.py     # API serializers
│   ├── views.py           # View controllers
│   ├── urls.py            # URL routing
│   └── templates/         # HTML templates
├── static/                # Static files (CSS, JS)
└── requirements.txt       # Project dependencies
```

## API Endpoints

- **Admin Authentication**:
  - POST `/api/admin/signup/`: Create a new admin account
  - POST `/api/admin/login/`: Login and receive an authentication token

- **Book Management**:
  - GET `/api/books/`: List all books
  - POST `/api/books/`: Create a new book (requires authentication)
  - GET `/api/books/{id}/`: Retrieve a specific book
  - PUT `/api/books/{id}/`: Update a book (requires authentication)
  - DELETE `/api/books/{id}/`: Delete a book (requires authentication)

## Web Interface

- `/signup`: Admin registration page
- `/login`: Admin login page
- `/books/`: Book management page (for admins)
- `/books/new/`: Add new book form
- `/books/edit/{id}/`: Edit book form
- `/student/`: Student view to browse books

## Assumptions

1. Book ISBNs are unique and used as identifiers
2. Admin authentication is email-based
3. Only authenticated admins can modify book data
4. Students only need read access to view books

