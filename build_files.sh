# build_files.sh
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

# make migrations
echo "Make Migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear

# createsuperuser
python3.9 manage.py createsuperuser
Username: demo
Email address:
Password: demo
Password (again): demo
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.