# build_files.sh
pip install -r requirements.txt
python3.10.8 manage.py collectstatic

python manage.py makemigrations
python manage.py migrate