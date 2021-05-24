# django_mfa2_example

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
