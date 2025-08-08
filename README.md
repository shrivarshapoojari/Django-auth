# Django AuthSystem - Role-Based Authentication

A complete Django authentication system with role-based user management supporting **Patient** and **Doctor** user types. Built with Django 5.2.4 and SQLite3, featuring a clean interface using raw HTML and CSS.

## 🚀 Features

### User Management
- **Two User Roles**: Patient and Doctor
- **Complete Registration**: First name, last name, username, email, password, address, and profile picture
- **Flexible Login**: Support for both username and email authentication
- **Role-Based Dashboards**: Separate interfaces for patients and doctors
- **Profile Pictures**: Image upload with proper handling

### Authentication Features
- ✅ User registration with validation
- ✅ Login/logout functionality
- ✅ Password confirmation validation
- ✅ Unique username and email validation
- ✅ Protected routes with `@login_required`
- ✅ Role-based redirection after login

### Technical Features
- ✅ Custom User model extending AbstractUser
- ✅ SQLite3 database
- ✅ Media file handling for uploads
- ✅ Responsive design with raw HTML/CSS
- ✅ Form validation and error handling

## 📋 Requirements

- Python 3.8+
- Django 5.2.4
- Pillow (for image handling)

## 🛠️ Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-authsystem.git
cd django-authsystem/AuthSystem
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📁 Project Structure

```
AuthSystem/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── accounts/
│   ├── models.py          # Custom User model
│   ├── views.py           # Authentication views
│   ├── forms.py           # Registration and login forms
│   ├── urls.py            # URL routing
│   ├── templates/         # HTML templates
│   │   ├── signup.html
│   │   ├── login.html
│   │   ├── patient_dashboard.html
│   │   └── doctor_dashboard.html
│   └── static/css/
│       └── style.css      # Raw CSS styling
├── AuthSystem/
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py
└── media/                 # User uploaded files
    └── profiles/
```

## 🎯 Usage

### User Registration
1. Navigate to `/signup/`
2. Fill in all required information
3. Select user type (Patient or Doctor)
4. Upload profile picture (optional)
5. Submit form

### User Login
1. Navigate to `/login/` or `/`
2. Enter username or email
3. Enter password
4. System redirects based on role:
   - Patients → `/patient_dashboard/`
   - Doctors → `/doctor_dashboard/`

### Dashboards
- **Patient Dashboard**: Shows patient information and available features
- **Doctor Dashboard**: Shows doctor information and medical portal features
- **Logout**: Available from any dashboard

## 🔒 Security Features

- Password validation and confirmation
- CSRF protection on all forms
- Login required decorators on protected views
- Unique email and username validation
- Secure file upload handling

## 📸 Screenshots

### Signup Page
Clean, responsive registration form with role selection.

### Login Page
Simple login interface supporting username or email.

### Patient Dashboard
Patient-focused interface showing personal information and available features.

### Doctor Dashboard
Doctor-focused interface with medical portal features.

## 🛡️ User Roles

### Patient
- Personal health information management
- Appointment scheduling access
- Medical record viewing
- Communication with healthcare providers

### Doctor
- Patient management capabilities
- Medical record access and updates
- Prescription management
- Patient communication tools

## 🔧 Customization

The application is built with modularity in mind:

- **Models**: Easily extend the CustomUser model
- **Templates**: Raw HTML/CSS for easy styling customization
- **Views**: Function-based views for straightforward modification
- **Forms**: Django forms with built-in validation

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Login page (home) |
| `/signup/` | GET/POST | User registration |
| `/login/` | GET/POST | User authentication |
| `/logout/` | GET | User logout |
| `/patient_dashboard/` | GET | Patient dashboard (protected) |
| `/doctor_dashboard/` | GET | Doctor dashboard (protected) |
| `/admin/` | GET | Django admin interface |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created with ❤️ for healthcare authentication systems.

## 🆘 Support

If you encounter any issues or have questions:

1. Review the Django documentation
2. Check the terminal for error messages
3. Open an issue on GitHub

## 🔄 Version History

- **v1.0.0** - Initial release with core authentication features
  - User registration and login
  - Role-based dashboards
  - Profile picture uploads
  - Local development ready

---

**Note**: This is a demo application designed for local development and learning purposes.
