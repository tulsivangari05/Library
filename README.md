**Django Library Management System**

A web-based Library Management System built using Django, designed to manage books efficiently with CRUD operations and a clean user interface.


**Features**

Add new books
Edit existing book details
Delete books
Django templates integration
SQLite database (default Django DB)


**Tech Stack**

Backend: Python, Django

Frontend: HTML, CSS

Database: SQLite


**Version Control:** Git & GitHub


**Project Structure**
Library/

├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py

├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   └── myapp/
│   │       ├── book_list.html
│   │       ├── add_book.html
│   │       └── edit_book.html
│   ├── models.py
│   ├── views.py
│   └── urls.py

├── db.sqlite3
├── manage.py
└── README.md


**Installation & Setup**

1. Clone the repository

2. Create virtual environment: python -m venv venv
                               venv\Scripts\activate   # Windows

3. Install dependencies: pip install django

4. Run migrations: python manage.py migrate

5. Start Server: python manage.py runserver

6. Open in browser: http://127.0.0.1:8000/books/


**Usage**

-Add, edit, or delete books using the UI

-All changes are reflected in the database instantly


**Live Demo**

Deployed on PythonAnywhere
🔗 Click here: https://tulsi05.pythonanywhere.com/
