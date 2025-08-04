# Django AuthSystem - PythonAnywhere Deployment Guide

## Prerequisites
1. Create a free account at https://www.pythonanywhere.com/
2. Upgrade to a paid account if you need custom domains or more resources

## Step-by-Step Deployment Instructions

### 1. Upload Your Code to PythonAnywhere

#### Option A: Using Git (Recommended)
```bash
# In PythonAnywhere console
git clone https://github.com/yourusername/your-repo.git
# OR upload your files manually
```

#### Option B: File Upload
1. Go to PythonAnywhere Dashboard → Files
2. Create a new directory: `/home/yourusername/AuthSystem/`
3. Upload all your project files to this directory

### 2. Set Up Virtual Environment
```bash
# In PythonAnywhere Bash console
cd /home/yourusername/
python3.10 -m venv authsystem_venv
source authsystem_venv/bin/activate
cd AuthSystem
pip install -r requirements.txt
```

### 3. Configure Database
```bash
# In your project directory with virtual environment activated
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Configure Static Files
```bash
# Add to settings.py
STATIC_ROOT = '/home/yourusername/AuthSystem/staticfiles/'

# Then run:
python manage.py collectstatic
```

### 5. Set Up Web App on PythonAnywhere
1. Go to PythonAnywhere Dashboard → Web
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10
5. Configure the following:

#### Source Code:
```
/home/yourusername/AuthSystem/
```

#### Working Directory:
```
/home/yourusername/AuthSystem/
```

#### WSGI Configuration File:
```
/var/www/yourusername_pythonanywhere_com_wsgi.py
```

Replace the contents of this file with:
```python
import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/AuthSystem'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AuthSystem.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### Virtual Environment:
```
/home/yourusername/authsystem_venv/
```

### 6. Configure Static Files Mapping
In the Web tab, add static files mapping:
- URL: `/static/`
- Directory: `/home/yourusername/AuthSystem/staticfiles/`

### 7. Configure Media Files Mapping
In the Web tab, add media files mapping:
- URL: `/media/`
- Directory: `/home/yourusername/AuthSystem/media/`

### 8. Update Settings for Production

Update `AuthSystem/settings.py`:
```python
# Replace 'yourusername' with your actual PythonAnywhere username
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = '/home/yourusername/AuthSystem/staticfiles/'
STATICFILES_DIRS = [
    '/home/yourusername/AuthSystem/accounts/static/',
]

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/yourusername/AuthSystem/media/'

# For production, set DEBUG = False (optional)
DEBUG = False  # Set to False for production
```

### 9. Reload Your Web App
1. Go back to the Web tab
2. Click the "Reload" button
3. Your app should now be live at `https://yourusername.pythonanywhere.com`

## Important Notes

### Security Considerations for Production:
1. **Change the SECRET_KEY** in settings.py to a new, secure value
2. **Set DEBUG = False** for production
3. **Update ALLOWED_HOSTS** to include only your domain
4. **Consider using environment variables** for sensitive settings

### File Permissions:
Ensure your media directory has proper write permissions:
```bash
chmod 755 /home/yourusername/AuthSystem/media/
chmod 755 /home/yourusername/AuthSystem/media/profiles/
```

### Troubleshooting:
1. **Check Error Logs**: Web tab → Log files → Error log
2. **Check Server Log**: Web tab → Log files → Server log
3. **Common Issues**:
   - Static files not loading: Check static files mapping
   - Database errors: Ensure migrations are run
   - Import errors: Check virtual environment is activated
   - Permission errors: Check file permissions

### Testing Your Deployment:
1. Visit `https://yourusername.pythonanywhere.com`
2. Test user registration (Patient and Doctor)
3. Test login functionality
4. Test file uploads (profile pictures)
5. Test dashboard access and logout

## Example URLs After Deployment:
- Home/Login: `https://yourusername.pythonanywhere.com/`
- Signup: `https://yourusername.pythonanywhere.com/signup/`
- Patient Dashboard: `https://yourusername.pythonanywhere.com/patient_dashboard/`
- Doctor Dashboard: `https://yourusername.pythonanywhere.com/doctor_dashboard/`
- Admin: `https://yourusername.pythonanywhere.com/admin/`

Replace 'yourusername' with your actual PythonAnywhere username throughout this guide.
