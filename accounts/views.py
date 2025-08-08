from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignupForm, UserLoginForm, BlogPostForm
from .models import CustomUser, BlogPost, BLOG_CATEGORIES

def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(f'/{user.role.lower()}_dashboard/')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    error = None
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']
            user = CustomUser.objects.filter(username=identifier).first() or \
                   CustomUser.objects.filter(email=identifier).first()
            if user:
                user = authenticate(username=user.username, password=password)
                if user:
                    login(request, user)
                    return redirect(f'/{user.role.lower()}_dashboard/')
            error = "Invalid credentials"
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import login_required

@login_required
def patient_dashboard(request):
    # Get all published blog posts (not drafts) categorized
    published_posts = BlogPost.objects.filter(is_draft=False)
    
    # Group posts by category
    posts_by_category = {}
    for category_code, category_name in BLOG_CATEGORIES:
        posts_by_category[category_name] = published_posts.filter(category=category_code)
    
    return render(request, 'patient_dashboard.html', {
        'user': request.user,
        'posts_by_category': posts_by_category
    })

@login_required
def doctor_dashboard(request):
    # Get doctor's own blog posts
    doctor_posts = BlogPost.objects.filter(author=request.user) if request.user.role == 'DOCTOR' else None
    
    return render(request, 'doctor_dashboard.html', {
        'user': request.user,
        'doctor_posts': doctor_posts
    })


# Blog Views
@login_required
def create_blog_post(request):
    if request.user.role != 'DOCTOR':
        messages.error(request, "Only doctors can create blog posts.")
        return redirect('doctor_dashboard')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            
            status = "draft" if blog_post.is_draft else "published"
            messages.success(request, f"Blog post '{blog_post.title}' has been saved as {status}.")
            return redirect('doctor_dashboard')
    else:
        form = BlogPostForm()
    
    return render(request, 'create_blog_post.html', {'form': form})

@login_required
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            blog_post = form.save()
            status = "draft" if blog_post.is_draft else "published"
            messages.success(request, f"Blog post '{blog_post.title}' has been updated as {status}.")
            return redirect('doctor_dashboard')
    else:
        form = BlogPostForm(instance=post)
    
    return render(request, 'edit_blog_post.html', {'form': form, 'post': post})

@login_required
def view_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    # Patients can only view published posts
    if request.user.role == 'PATIENT' and post.is_draft:
        messages.error(request, "This blog post is not available.")
        return redirect('patient_dashboard')
    
    # Doctors can only view their own drafts or any published posts
    if request.user.role == 'DOCTOR' and post.is_draft and post.author != request.user:
        messages.error(request, "This blog post is not available.")
        return redirect('doctor_dashboard')
    
    return render(request, 'view_blog_post.html', {'post': post})

@login_required
def blog_category_view(request, category):
    # Map category slugs to category codes
    category_mapping = {
        'mental-health': 'MENTAL_HEALTH',
        'heart-disease': 'HEART_DISEASE', 
        'covid-19': 'COVID19',
        'immunization': 'IMMUNIZATION'
    }
    
    category_code = category_mapping.get(category.lower())
    if not category_code:
        messages.error(request, "Category not found.")
        return redirect('patient_dashboard')
    
    # Get category name for display
    category_name = dict(BLOG_CATEGORIES)[category_code]
    
    # Get published posts in this category
    posts = BlogPost.objects.filter(category=category_code, is_draft=False)
    
    return render(request, 'blog_category.html', {
        'posts': posts,
        'category_name': category_name,
        'category': category
    })
