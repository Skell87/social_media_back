# Generated by Django 5.0.6 on 2024-06-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_back_app', '0002_userpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
