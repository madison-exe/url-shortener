# Generated by Django 3.0.3 on 2025-03-19 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=500)),
                ('short_url', models.CharField(max_length=50)),
            ],
        ),
    ]
