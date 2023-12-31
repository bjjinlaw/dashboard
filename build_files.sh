# build_files.sh
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

# make migrations
echo "Make Migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py makemigrations usermanagement
python3.9 manage.py makemigrations userprofile
python3.9 manage.py makemigrations faculty
python3.9 manage.py migrate --noinput
python3.9 manage.py migrate usermanagement
python3.9 manage.py migrate userprofile
python3.9 manage.py migrate faculty

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear

