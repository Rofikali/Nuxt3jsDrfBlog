# Generated by Django 5.0 on 2024-02-10 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
    ]