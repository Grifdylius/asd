# Generated by Django 3.2.9 on 2022-08-30 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy_apps', '0009_auto_20220829_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='carausel',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Краткая биография'),
        ),
    ]