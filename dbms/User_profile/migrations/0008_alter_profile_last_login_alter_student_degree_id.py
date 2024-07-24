# Generated by Django 5.0.4 on 2024-04-28 20:03

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_profile', '0007_remove_student_course_id_student_degree_id_and_more'),
        ('acadamic', '0004_alter_courses_degree_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 1, 33, 57, 316436), verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='student',
            name='degree_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acadamic.degree', verbose_name='Degree'),
        ),
    ]