# django_mfa2_example

Fingerprint-based authentication and authorization system in Python (Django). This can be integrated with e-voting systems and other applications that should be very secure. 

A walk-through of this repository can be found on [dev.to](https://dev.to/) in this tutorial-like article [Fingerprint-based authentication and authorization in Python(Django) web applications](
https://dev.to/sirneij/fingerprint-based-authentication-and-authorization-in-python-django-web-applications-2c6l).
This example application uses [Django-mfa2](https://github.com/mkalioby/django-mfa2) to implement a password-less fingerprint-based authentication and authorization system. It's live and can be accessed [here](https://django-mfa2-example.herokuapp.com/).
## Run locally

- clone this report:
  ```
  git clone https://github.com/Sirneij/django_mfa2_example.git
  ```
- create and activate virtual environment (I used `pipenv` but you can stick with `venv`, `virtualenv` or `poetry`):
  ```
  pipenv shell
  pipenv install
  ```
- makemigrations and migrate:
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
- optionally, createsuperuser:
  ```
  python manage.py createsuperuser
  ```
