echo "BUILD START"
pip install --upgrade pip
pip3 install -r requirements.txt
python manage.py migrate 
python manage.py collectstatic
echo "BUILD END"