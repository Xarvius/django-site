# Generated by Django 3.0.6 on 2020-09-24 11:35

from django.db import migrations, models
import user_manage.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0013_auto_20200923_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='file',
            field=models.FileField(default='-', upload_to=user_manage.models.user_directory_path),
        ),
    ]