echo "BUILD START"
pip install --upgrade
pip install python3-dev
sudo apt install libpq-dev libpq-dev
pip3 install -r requirements.txt
python3.9 manage.py collectstatic

echo "BUILD END"