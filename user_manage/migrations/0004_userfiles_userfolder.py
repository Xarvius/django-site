# Generated by Django 3.0.6 on 2020-07-30 11:52

from django.db import migrations, models
import django.db.models.deletion
import user_manage.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0003_auto_20200729_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_manage.UserFolder')),
            ],
        ),
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('file', models.FileField(upload_to=user_manage.models.user_directory_path)),
                ('folder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_manage.UserFolder')),
            ],
        ),
    ]
