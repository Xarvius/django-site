from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
    Engineer = "ST"
    PROFESSOR = "PROF."
    STATUS_IN = [
        (Engineer, 'Inżynier'),
        ('lic.', "Licencjat"),
        ('mgr', "Magister"),
        ('mgr inż.', "Magister inżyner"),
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


