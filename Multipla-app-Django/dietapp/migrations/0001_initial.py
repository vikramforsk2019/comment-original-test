# Generated by Django 3.0.5 on 2020-11-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('group', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('postfile', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'health_data',
            },
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('uname', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('pic', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'signup',
            },
        ),
    ]