courses/                        # Root project directory
├── courses/                   # Project settings directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── coursesR/                  # Application directory
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/                    # Directory for static files (CSS, JS)
│   ├── styles.css
│   └── scripts.js
├── templates/                 # Directory for HTML templates
│   ├── base.html
│   └── coursesR/
│       ├── course_list.html
│       └── course_detail.html
├── db.sqlite3                 # SQLite database file
├── manage.py                  # Django management script
└── requirements.txt           # File to list project dependencies (optional)
