from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
def user_directory_path(instance, filename):
    return f'user_files/user_{instance.user.id}/{filename}'

class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254, default="-")
    Engineer = "inz."
    PROFESSOR = "PROF."
    STATUS_IN = [
        (Engineer, 'Inżynier'),
        ('lic.', "Licencjat"),
        ('mgr', "Magister"),
        ('mgr inz.', "Magister inżyner"),
        ('dr', "Doktor"),
        ('dr hab.', "Doktor habilitowany"),
        ('prof.', "Profesor"),
    ]
    qualification = models.CharField(
        max_length=8,
        choices=STATUS_IN,
        default=Engineer
    )
    USOSlink = models.URLField(max_length=200, default="-")

    def __str__(self):
        return self.user.username

class UserFolder(models.Model):
    name = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserFiles(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    folder = models.ForeignKey('UserFolder', null=True, on_delete=models.CASCADE)

class UserExtras(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intro = models.TextField()
    extras = models.TextField()
    education = models.TextField()
    hobbies = models.TextField()

class Results(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=30)
    file = models.FileField(upload_to=user_directory_path, default="-")

class UserPublications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.TextField()

# class UserOptions(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     results = models.BooleanField(**options)
#     menu