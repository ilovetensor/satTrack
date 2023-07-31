echo "BUILD START"
pip install --upgrade pip
pip3 install -r requirements.txt
python3.9 manage.py migrate 
python3.9 manage.py collectstatic
echo "BUILD END"