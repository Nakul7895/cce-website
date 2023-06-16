# Generated by Django 3.2.17 on 2023-06-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentservices', '0004_nssabout'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitallibrary',
            name='description',
            field=models.TextField(default='nil'),
        ),
        migrations.AddField(
            model_name='digitallibrary',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='digitallibrary',
            name='link',
            field=models.CharField(default='www', max_length=100),
        ),
    ]
