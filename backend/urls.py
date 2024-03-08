from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    # Admin URL for Django Admin Panel
    path('admin/', admin.site.urls),

    # Home URL
    path('', views.home, name='home'),

    # API URLs
    path('api/categories/', views.categories_list, name='categories-list'),  # Endpoint for retrieving categories list
    path('api/posts/', views.posts_list, name='posts-list'),  # Endpoint for retrieving list of posts
    path('api/posts/<int:pk>/', views.posts_detail, name='posts-detail'),  # Endpoint for retrieving a specific post
]
