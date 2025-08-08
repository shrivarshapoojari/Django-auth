from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, BlogPost
from django.core.exceptions import ValidationError

# User Signup Form
class UserSignupForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'})
    )

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name',
            'profile_picture',
            'username', 'email',
            'role',
            'address_line1', 'city', 'state', 'pincode',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'role': forms.RadioSelect(),
            'address_line1': forms.TextInput(attrs={'placeholder': 'Address Line 1'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'pincode': forms.TextInput(attrs={'placeholder': 'Pincode'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("password1")
        pwd2 = cleaned_data.get("password2")
        if pwd1 and pwd2 and pwd1 != pwd2:
            raise ValidationError("Passwords do not match.")
        return cleaned_data


# User Login Form (username or email)
class UserLoginForm(forms.Form):
    identifier = forms.CharField(
        label='Username or Email',
        widget=forms.TextInput(attrs={'placeholder': 'Username or Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        label='Password'
    )


# Blog Post Form for Doctors
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter blog post title',
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={
                'placeholder': 'Enter a brief summary of your blog post...',
                'rows': 4,
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your full blog post content here...',
                'rows': 10,
                'class': 'form-control'
            }),
            'is_draft': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        labels = {
            'is_draft': 'Save as draft',
        }
