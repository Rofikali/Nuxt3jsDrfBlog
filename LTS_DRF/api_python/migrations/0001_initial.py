# Generated by Django 5.0 on 2024-01-17 07:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PythonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(default='Admin', on_delete=django.db.models.deletion.CASCADE, related_name='python_post_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PythonModel',
                'verbose_name_plural': 'PythonModels',
            },
        ),
    ]
