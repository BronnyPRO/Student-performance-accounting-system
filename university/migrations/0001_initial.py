# Generated by Django 5.0.6 on 2024-05-30 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Math', 'Math'), ('Physics', 'Physics'), ('Music', 'Music')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.students')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.subjects')),
            ],
        ),
    ]
