## source: 
https://www.youtube.com/watch?v=Sa_kQheCnds&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=13
https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

### plotly
https://www.youtube.com/watch?v=TcnWEQMT3_A
## python venv
https://realpython.com/python-virtual-environments-a-primer/#activate-it

sudo apt install python3-venv

python3 -m venv ./django_project/.venv
source .venv/bin/activate


## requirements
pip freeze > requirements.txt
pip install -r requirements.txt

## Setting.py on server
./manage.py collectstatic


## apache2
/etc/apache2/sites-available/django_project.conf 
$ sudo a2ensite django_project.conf
$ sudo a2dissite 000-default.conf 

## permissions
sudo chown -R :www-data wietse
sudo chown :www-data django_project/db.sqlite3 
sudo chmod 664 django_project/db.sqlite3 
sudo chown :www-data django_project/
sudo chown -R :www-data django_project/media/
sudo chmod -R 775 django_project/media/

## securing

sudo touch ./settings.json

## Reload

```sh
sudo killall lswsgi
```