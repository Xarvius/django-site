from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_register/', views.register, name='user_register'),
    path('user_profile/', views.user_profile, name='user_profile'),
]
