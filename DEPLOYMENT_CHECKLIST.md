# Quick Deployment Checklist for PythonAnywhere

## Files Ready for Upload:
✅ All source code files
✅ requirements.txt
✅ DEPLOYMENT_GUIDE.md
✅ staticfiles/ directory (after collectstatic)
✅ media/ directory structure

## Pre-Deployment Commands (run locally):
```bash
python manage.py collectstatic --noinput
python manage.py makemigrations
```

## PythonAnywhere Setup Steps:
1. [ ] Create PythonAnywhere account
2. [ ] Upload project files to `/home/yourusername/AuthSystem/`
3. [ ] Create virtual environment and install requirements
4. [ ] Run migrations and create superuser
5. [ ] Configure web app (Manual configuration, Python 3.10)
6. [ ] Set up WSGI file
7. [ ] Configure static files mapping
8. [ ] Configure media files mapping
9. [ ] Update ALLOWED_HOSTS in settings.py
10. [ ] Reload web app

## Quick Commands for PythonAnywhere Console:
```bash
# Set up virtual environment
python3.10 -m venv authsystem_venv
source authsystem_venv/bin/activate

# Install dependencies
cd AuthSystem
pip install -r requirements.txt

# Set up database
python manage.py migrate
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

## Test URLs After Deployment:
- https://yourusername.pythonanywhere.com/ (Login)
- https://yourusername.pythonanywhere.com/signup/ (Signup)
- https://yourusername.pythonanywhere.com/admin/ (Admin)
