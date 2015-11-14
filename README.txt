# Run local server
python manage.py runserver

# Sync databse
python manage.py syncdb

# Generate translations
python manage.py makemessages -l es

# Compile tranlsations 
python manage.py compilemessages -l es

# Open Shift Server
rhc setup
rhc ssh -a eba
# Install django
pip install django
exit
# Deploy application
rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=eba/wsgi.py --app eba 
Root User: adminzbqagqe
Root Password: _rCi5MSACkIJ
Database Name: eba

Connection URL: postgresql://$OPENSHIFT_POSTGRESQL_DB_HOST:$OPENSHIFT_POSTGRESQL_DB_PORT

#Backup database
rhc scp eba download . /var/lib/openshift/562e30530c1e66bf84000050/app-root/repo/db.sqlite3
