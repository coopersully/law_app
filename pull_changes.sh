#!/bin/bash

# Navigate to your Django project directory
cd /var/www/law_app || exit

# Pull the latest changes from the repository
git pull

# Perform database migrations and collect static files
python manage.py migrate
python manage.py collectstatic --noinput

# Restart Apache2 to apply the changes
sudo systemctl restart apache2
