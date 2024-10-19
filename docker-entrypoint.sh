#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Wait for the PostgreSQL database to be ready
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for PostgreSQL..."

    while ! nc -z "$DATABASE_HOST" "$DATABASE_PORT"; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files (if applicable)
# echo "Collecting static files..."
# python manage.py collectstatic --noinput

# Start the Django development server
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
