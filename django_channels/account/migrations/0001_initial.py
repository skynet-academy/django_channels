# Generated by Django 4.0.3 on 2022-03-16 08:52

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('data_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_join', models.DateTimeField(auto_now_add=True, verbose_name='last join')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, default=account.models.get_default_profile_image, max_length=255, null=True, upload_to=account.models.get_profile_image_filepath)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
