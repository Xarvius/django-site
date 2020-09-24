from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_register/', views.register, name='user_register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('upload_files/', views.upload_files, name='upload_files'),
    path('create_folder/', views.create_folder, name='create_folder'),
    path('user_extras/', views.create_extras, name='create_extras'),
    path('exam_results/', views.upload_results, name='upload_results'),
    path('user_publications/', views.create_publications, name='create_publications'),
]
