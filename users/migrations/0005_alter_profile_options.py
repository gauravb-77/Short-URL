# Generated by Django 5.0.3 on 2024-03-23 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]
