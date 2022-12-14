# Generated by Django 3.2.9 on 2022-08-20 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy_apps', '0004_auto_20220513_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Имена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Учителя',
                'verbose_name_plural': 'Учителей',
            },
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Post_rus',
        ),
    ]
