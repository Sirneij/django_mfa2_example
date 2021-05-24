# django_mfa2_example

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
