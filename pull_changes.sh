#!/bin/bash

# Navigate to your Django project directory
cd /var/www/law_app || exit

# Pull the latest changes from the repository
git pull

# Activate the virtual environment
source /var/www/law_app/venv/bin/activate

# Install all requirements
pip install -r requirements.txt

# Perform database migrations and collect static files
python manage.py migrate
python manage.py collectstatic --noinput

# Restart the Uvicorn service
sudo /bin/systemctl restart uvicorn_law_app
