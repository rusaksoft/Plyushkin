kill $(ps aux | grep manage.py | awk '{print $2}')
python manage.py runserver 0.0.0.0:8000 &