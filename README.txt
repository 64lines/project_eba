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
