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
--username demo
--password demo
