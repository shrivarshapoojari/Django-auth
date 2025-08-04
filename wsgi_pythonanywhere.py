# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.

import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/AuthSystem'  # Replace 'yourusername' with your actual PythonAnywhere username
if path not in sys.path:
    sys.path.insert(0, path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AuthSystem.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
