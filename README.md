# api_django_app
 
# HOW TO UPDATE YUM IN CENTOS #

sudo yum install epel-release
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
sudo yum -y -q install httpd mod_ssl httpd-devel
sudo yum -y -q groupinstall development
sudo yum -y -q install zlib2-devel openssl-devel sqlite-devel bzip2-devel python-devel openssl-devel openssl-perl libjpeg-turbo libjpeg-turbo-devel zlib-devel giflib ncurses-devel gdbm-devel xz-devel tkinter readline-devel tk tk-devel kernel-headers glibc libpng gcc-c++

# HOW TO COMPILE LATEST PYTHON WITH ISOLATED ENV # 
mkdir .venv
cd .venv
sudo yum install -y openssl11-devel # install ssl
sudo yum install -y centos-release-scl # upgrade gcc
sudo yum install -y devtoolset-7
scl enable devtoolset-7 bash # enable gcc
curl -O https://www.python.org/ftp/python/3.12.1/Python-3.12.1.tgz # install python from source code
tar -xzf Python-3.12.1.tgz
cd Python-3.12.1
sed -i 's/PKG_CONFIG openssl /PKG_CONFIG openssl11 /g' configure
./configure --enable-optimizations --enable-shared --prefix=/home/hazrina/.venv LDFLAGS="-Wl,-rpath=/home/hazrina/.venv/lib" # compile python from source code
make altinstall
cd ..
echo $SHELL #check shell
env #check env
export PATH="/home/hazrina/.venv/bin" #export path
printf "%s\n" $PATH #check path
bin/python3.12 -m venv dj-env
source dj-env/bin/activate
python -m pip install django
python -m django --version

# HOW TO COMPILE MOD WGSI #

wget -O mod_wsgi-5.0.0.tar.gz https://github.com/GrahamDumpleton/mod_wsgi/archive/refs/tags/5.0.0.tar.gz
tar xvfz mod_wsgi-5.0.0.tar.gz
cd mod_wsgi-5.0.0
./configure LDFLAGS='-Wl,-rpath=/home/hazrina/.venv/lib' --with-python=/home/hazrina/.venv/bin/python3.12
make
sudo make install

# HOW TO START DJANGO PROJECT #

django-admin startproject mysite
sudo mv mysite project_name
cd project_name
python manage.py runserver
python manage.py startapp app-name

# HOW TO CONFIGURE APACHE FOR MOD WGSI #

## CONFIGURE httpd.conf ##
sudo vim /etc/httpd/conf/httpd.conf
> add to httpd.conf
LoadModule wsgi_module modules/mod_wsgi.so

## CONFIGURE django.conf ##
sudo vim /etc/httpd/conf.d/django.conf
> add to django.conf
WSGIScriptAlias /project_name /pathto/wsgi.py
WSGIPythonHome /pathto/dj-env

Alias /static /pathto/static
<Directory / /static>
    Require all granted
</Directory>
<Directory /pathto/media>
    Require all granted
</Directory>
<Directory /pathto/mysite>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>
WSGIDaemonProcess mfrlab python-home=/pathto/.venv/dj-env python-path=/pathto
WSGIProcessGroup mfrlab
WSGIApplicationGroup %{GLOBAL}
WSGIPassAuthorization On

## SET PERMISSIONS ##
chmod 775 -R mysite
chmod 775 manage.py

## INSTALL DEPENDENCIES ##
python -m pip install django-groupadmin-users
python -m pip install djangorestframework
python -m pip install django-crispy-forms
python -m pip install psycopg2-binary
python -m pip install requests
python -m pip install pandas
python -m pip install setuptools
python -m pip install django-serverside-datatable
python -m pip install sendgrid-django
python -m pip install geopy
python -m pip install transformers
python -m pip install crispy-bootstrap4
python -m pip install django-simple-history
python -m pip install openpyxl
python -m pip install pyxlsb
python -m pip install psycopg2
python -m pip install scikit-learn


# HOW TO REFRESH DJANGO APPLICATION AFTER FILE UPDATE #
touch ~/pathto/wsgi.py # soft refresh
OR
sudo apachectl restart # brute refresh

# HOW TO READ APACHE LOG FILE FOR TROUBLESHOOTING #
sudo tail -30 /etc/httpd/logs/error_log # print last 30 lines

# HOW TO MAKE MIGRATION IN DJANGO APPLICATION #

cd ~/project_name
source ../.venv/dj-env/bin/activate
python manage.py makemigrations app-name
python manage.py migrate

# HOW TO REDO MIGRATION IN DJANGO APPLICATION #

cd ~/project_name
source ../.venv/dj-env/bin/activate
rm -rf path/to/migration_file_that_have_error.py
python manage.py makemigrations app-name
python manage.py migrate

# HOW TO RESET DJANGO SEQUENCE TABLES FOR APP MODELS #

cd ~/project_name
source ../.venv/dj-env/bin/activate
python manage.py shell
> python
from django.core.management.color import no_style
from django.db import connection
> import models
sequence_sql = connection.ops.sequence_reset_sql(no_style(), [model1,model2])
with connection.cursor() as cursor:
    for sql in sequence_sql:
        cursor.execute(sql)

# HOW TO ACCESS POSTGRESQL #

sudo -u postgres -i # open subshell (password prompt: server password)
psql




