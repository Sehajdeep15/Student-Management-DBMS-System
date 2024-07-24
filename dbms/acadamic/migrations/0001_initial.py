# Generated by Django 5.0.4 on 2024-04-28 19:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('degree_id', models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='course id')),
                ('degree_name', models.CharField(default='s', max_length=200, verbose_name='course name')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='subject id')),
                ('course_name', models.CharField(default='s', max_length=200, verbose_name='subject name')),
                ('degree_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='acadamic.degree')),
            ],
        ),
        migrations.CreateModel(
            name='sessions',
            fields=[
                ('session_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='session id')),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='from')),
                ('end_date', models.DateField(default=datetime.date.today, verbose_name='to')),
                ('degree_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acadamic.degree')),
            ],
        ),
    ]