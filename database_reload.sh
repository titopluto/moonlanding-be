#rm db.sqlite3
find moonlightapp/migrations/ -type f -name "*.py" | grep -v "__init__.py" | xargs rm # cd moonlightapp/migrations/ && rm -- !(__init__.py)
python manage.py makemigrations
python manage.py migrate
#python manage.py createsuperuser
