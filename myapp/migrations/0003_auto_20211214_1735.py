# Generated by Django 3.2 on 2021-12-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_filetugas_filenya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tugas',
            name='kelas',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tugas',
            name='nama',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tugas',
            name='nim',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tugas',
            name='subjek',
            field=models.CharField(max_length=100, null=True),
        ),
    ]