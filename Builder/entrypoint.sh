echo "⏳ Waiting for MySQL at $DB_HOST:$DB_PORT..."
until nc -z $DB_HOST $DB_PORT; do
  sleep 1
done
echo "✅ MySQL is up!"

echo "🚀 Running migrations..."
python manage.py migrate account admin auth contenttypes sessions socialaccount

echo "🟢 Starting Django..."
python manage.py runserver 0.0.0.0:8000
