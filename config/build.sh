echo "BUILD START"
pip install --upgrade pip
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate 
python manage.py createsuperuser --no-input
python manage.py collectstatic
echo "BUILD END"