# Generated by Django 3.0.3 on 2025-03-20 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_url_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='created_at',
            new_name='created_on',
        ),
    ]
