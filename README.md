
Tutorial "django plants" website written in Django.

----

This web application creates an online catalog for NM rare plants, where users can browse plants with photos in details section.

The main features that have currently been implemented are:

* There are models for plant and plantphoto.
* Users can view list and detail information for plant.
* Admin users can create and manage models. 

get source from https://github.com/rastogiunm)

Follow these instructions to configure your environment:
--------------------

settings.py

move secret key to environment variable
1. 
SECRET_KEY = os.environ['SECRET_KEY']
nano ~/.bash_profile
add this line to the end of file and save and exit
export SECRET_KEY="yoursecretkeyhere"

source ~/.bash_profile

2.
nano /usr/local/etc/my.cnf

add these lines to the end of file
Only allow connections from localhost

bind-address = 127.0.0.1
[client]
database = nmrareplants_db
user = admin
password = yourpwd
default-character-set = utf8

--------------------
source my_env/bin/activate

python manage.py createsuperuser

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

--------------------
for testing

python manage.py collectstatic
python manage.py test --verbosity 2

--------------------
brew services start mysql
mysql -u root -p

python manage.py check --deploy


--------------------
…or create a new repository on the command line

echo "# djangoplants" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/rastogiunm/djangoplants.git
git push -u origin master
…or push an existing repository from the command line

git remote add origin https://github.com/rastogiunm/djangoplants.git
git push -u origin master
…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.