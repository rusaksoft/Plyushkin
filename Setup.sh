sudo apt-get update
sudo apt-get install python-pip -y
sudo pip install django
cd /var/Plyushkin

#for duplicity
sudo apt-get install python-lockfile -y
sudo apt-get install librsync-dev -y
sudo apt-get install python-dev -y

cd duplicity
./compilec.py

sudo apt-get install lftp -y
sudo apt-get install git -y
sudo pip install git+https://github.com/rusaksoft/schedule

cd /var/Plyushkin
python manage.py migrate

echo "*/10 * * * * python /var/Plyushkin/manage.py runmonitor" | crontab -

python manage.py runserver 0.0.0.0:8000 &

#python manage.py startapp monitoring
#python manage.py createsuperuser
