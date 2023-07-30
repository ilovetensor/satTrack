echo "BUILD START"
pip install --upgrade pip
pip install python3-dev
pip3 install -r requirements.txt
python3.9 manage.py collectstatic
python3.9 manage.py makemigrations
python3.9 manage.py migrate

echo "BUILD END"