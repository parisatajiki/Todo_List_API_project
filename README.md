#  Todo List API with Authentication

A RESTful API built with Django REST Framework for managing a personal to-do list.  
This project includes **user authentication**, **authorization**, **pagination**, and **filtering** in addition to basic CRUD operations.

https://roadmap.sh/projects/todo-list-api

---

##  Features
- User Registration & Login
- Token-based Authentication
- CRUD Operations for to-do items
- Pagination & Filtering
- Secure Password Hashing
- Error Handling & Data Validation
- Database Integration

---


## Setup

git clone https://github.com/yourusername/todo-list-api.git
cd todo-list-api
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
