# Generated by Django 3.2.17 on 2023-06-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentservices', '0003_alter_centrallibrary_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NssAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='nss/icon')),
            ],
        ),
    ]
