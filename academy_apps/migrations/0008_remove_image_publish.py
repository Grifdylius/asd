# Generated by Django 3.2.9 on 2022-08-20 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy_apps', '0007_auto_20220820_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='publish',
        ),
    ]
