

echo "🚀 Running migrations..."
python manage.py migrate account admin auth contenttypes sessions socialaccount

echo "🟢 Starting Django..."
python manage.py runserver 0.0.0.0:8000
