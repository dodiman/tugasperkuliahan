# Generated by Django 3.2 on 2021-12-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filetugas',
            name='filenya',
            field=models.FileField(upload_to='file/%Y/%m/%d'),
        ),
    ]
