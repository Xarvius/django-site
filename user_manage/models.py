from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
    STUDENT = "ST"
    PROFESOR = "PROF"
    STATUS_IN = [
        (STUDENT, 'STUDENT'),
        (PROFESOR, "PROFESOR")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    date_begin = models.DateField(default=datetime.today)
    status = models.CharField(
        max_length=4,
        choices=STATUS_IN,
        default=PROFESOR
    )

    def __str__(self):
        return self.user.username
