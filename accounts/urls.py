from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    
    # Blog URLs
    path('create-blog-post/', views.create_blog_post, name='create_blog_post'),
    path('edit-blog-post/<int:post_id>/', views.edit_blog_post, name='edit_blog_post'),
    path('blog-post/<int:post_id>/', views.view_blog_post, name='view_blog_post'),
    path('blog/category/<str:category>/', views.blog_category_view, name='blog_category'),
]
