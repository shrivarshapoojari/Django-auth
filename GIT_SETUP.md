# Git Setup and GitHub Push Guide

## Quick Commands to Push to GitHub

### 1. Initialize Git Repository (if not already done)
```bash
cd "d:\Full Stack\jangoauth\AuthSystem"
git init
```

### 2. Add All Files
```bash
git add .
```

### 3. Check What Will Be Committed
```bash
git status
```

### 4. Make Initial Commit
```bash
git commit -m "Initial commit: Django AuthSystem with role-based authentication"
```

### 5. Create GitHub Repository
1. Go to https://github.com/
2. Click "New repository"
3. Name it `django-authsystem` (or your preferred name)
4. Don't initialize with README (we already have one)
5. Click "Create repository"

### 6. Add Remote Origin
```bash
git remote add origin https://github.com/YOUR_USERNAME/django-authsystem.git
```

### 7. Push to GitHub
```bash
git branch -M main
git push -u origin main
```

## Files That Will Be Included (✅) and Excluded (❌)

### ✅ Included Files:
- All Python source code (.py files)
- Templates (.html files)
- Static files (.css files)
- Requirements.txt
- README.md
- DEPLOYMENT_GUIDE.md
- DEPLOYMENT_CHECKLIST.md
- .gitignore

### ❌ Excluded Files (via .gitignore):
- __pycache__/ directories
- db.sqlite3 (database file)
- media/ directory (uploaded files)
- staticfiles/ directory
- Virtual environment (venv/)
- .env files
- Log files
- IDE settings (.vscode/, .idea/)

## Important Notes

1. **Database**: The SQLite database file (`db.sqlite3`) is excluded. Users will need to run migrations after cloning.

2. **Media Files**: Uploaded profile pictures are excluded. The directory structure will be created when users upload files.

3. **Environment Variables**: If you add any secrets later, use environment variables and .env files (which are gitignored).

4. **Virtual Environment**: Each user should create their own virtual environment using `requirements.txt`.

## Example Repository Structure on GitHub:
```
django-authsystem/
├── README.md
├── .gitignore
├── requirements.txt
├── DEPLOYMENT_GUIDE.md
├── DEPLOYMENT_CHECKLIST.md
├── manage.py
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
└── AuthSystem/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## After Pushing to GitHub

### For New Users Cloning Your Repository:
```bash
git clone https://github.com/YOUR_USERNAME/django-authsystem.git
cd django-authsystem
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Keep Repository Updated:
```bash
# After making changes
git add .
git commit -m "Description of changes"
git push origin main
```
