from django.contrib import admin
from .models import CustomUser, BlogPost

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'date_joined')
    list_filter = ('role', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_draft', 'created_at', 'updated_at')
    list_filter = ('category', 'is_draft', 'created_at', 'author')
    search_fields = ('title', 'summary', 'content')
    readonly_fields = ('created_at', 'updated_at')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Non-superuser doctors can only see their own posts
        if hasattr(request.user, 'role') and request.user.role == 'DOCTOR':
            return qs.filter(author=request.user)
        return qs.none()
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new object
            obj.author = request.user
        super().save_model(request, obj, form, change)
