
pip install -r requirements.txt

gunicorn -c gun.conf sever:app