# Dynamic Portfolio - Django Web App

A fully functional and customizable portfolio website built using Django. This project allows showcasing projects, skills, and education while enabling user interactions through a contact form and admin dashboard.

## Live Demo

Hosted on Render:  
https://portfolio-website-suh3.onrender.com

---

## Features

- Dynamic sections: Projects, Skills, About, Experience, Education
- Contact form with email notifications
- Admin panel for managing content
- Dashboard with basic analytics
- Light/Dark mode toggle
- Language switcher (i18n)
- Secure with environment-based configuration

---

## Technologies Used

- Python 3.11
- Django 5.2
- SQLite3
- Gunicorn (production WSGI server)
- WhiteNoise (static files)
- Render (deployment)

---

## Project Structure
portfolio/
├── manage.py
├── portfolio/ # Django root project
├── port_folio/ # Main app
├── templates/
├── static/
├── requirements.txt
├── .env # For environment variables (not committed)
└── README.md

---

## Local Setup
``` bash 
# Clone the repository
git clone https://github.com/Jenil7828/Dynamic-Portfolio.git
cd Dynamic-Portfolio

# Create a virtual environment
python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run the development server
python manage.py runserver

SECRET_KEY=your_django_secret_key
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

## Contact and Messages
Messages submitted through the contact form are saved in the database.
Messages are also emailed to the admin email set in the environment variables.

License
This project is licensed under the MIT License.

Developed by Jenil Rathod
GitHub: https://github.com/Jenil7828
