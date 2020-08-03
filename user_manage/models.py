from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
def user_directory_path(instance, filename):
    return f'user_files/user_{instance.user.id}/{filename}'

class UserProfile(models.Model):
    Engineer = "inz"
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    date_begin = models.DateField(default=datetime.today)
    qualification = models.CharField(
        max_length=8,
        choices=STATUS_IN,
        default=Engineer
    )
    education = models.TextField(default='-')
    publications = models.TextField(default='-')
    extras = models.TextField(default='-')

    def __str__(self):
        return self.user.username

class UserFolder(models.Model):
    name = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserFiles(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    folder = models.ForeignKey('UserFolder', null=True, on_delete=models.CASCADE)



