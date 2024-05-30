# courseR

Welcome to the courseR repository! This project is the final project for CS50web and is a dynamic web application built using Django. Below you will find information about the project's distinctiveness and complexity, the contents of each file, how to run the application, and additional notes for the staff.   

  # vid demo
[![Watch the video](https://github.com/Raufjatoi/courseR/blob/main/Screenshot%202024-05-30%20115218.png)](https://youtu.be/tnAO7Iutefs?si=iBM767odHPa3UOWR) click it 🙂       

#medium article 🥸  
[![medium article](https://github.com/Raufjatoi/courseR/blob/main/courseR.png)](https://medium.com/@raufpokemon00/courser-my-final-project-for-cs50web-744078c7ea41) same 🙂        

## Distinctiveness and Complexity

### Distinctiveness
This project is distinct because it provides a comprehensive course management system that includes functionalities for user registration, login, logout, and course creation. Unlike basic Django projects, this application involves advanced features such as dynamic content updates and user-specific actions. The project is designed to be user-friendly while also demonstrating the power of Django in handling complex web applications.

### Complexity
The complexity of this project lies in its dynamic nature and the integration of multiple user roles (admin and general users). Key features include:
- User authentication and authorization
- Dynamic course creation and display
- Real-time content updates
- Administrative controls through Django's admin panel

These elements require a deep understanding of Django's models, views, and templates, as well as handling user sessions and permissions.

## File Structure and Contents

### Project Files
- `manage.py`: The command-line utility for administrative tasks.
- `requirements.txt`: A list of Python packages required to run the project.
- `README.md`: This readme file.
- `structure.sql` : when i start i start with some structure like this then again i do some changes 

### Application Files (within your Django app directory)
- `settings.py`: Configuration for the Django project.
- `urls.py`: URL declarations for the project.
- `views.py`: Contains the logic for handling requests and rendering responses.
- `models.py`: Defines the database schema for the application.
- `admin.py`: Configuration for the Django admin interface.
- `templates/`: HTML templates for rendering the web pages.
- `static/`: Static files (CSS, JavaScript, images) used in the project.

### Templates
- `base.html`: The base template with common HTML structure.
- `index.html`: The home (welcome) page.
- `login.html`: The user login page.
- `register.html`: The user registration page.
- `courses.html`: The page displaying available courses.

## How to Run Your Application

To run this application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Raufjatoi/courseR.git
   cd courses

2. pip install -r  requirements.txt      

3. python manage.py makemigrations
   python manage.py migrate   

4. python manage.py 
   createsuperuser

5. python manage.py runserver  

Tadaaa 😁 
 
