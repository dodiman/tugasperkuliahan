# Generated by Django 3.2 on 2021-12-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20211215_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_subjek', models.CharField(max_length=100, unique=True)),
                ('batas_waktu', models.DateTimeField()),
                ('matakuliah', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tugas',
            name='subjek',
        ),
        migrations.AddField(
            model_name='tugas',
            name='subjeks',
            field=models.ManyToManyField(to='myapp.Subjek'),
        ),
    ]