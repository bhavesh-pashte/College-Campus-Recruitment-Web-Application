# Generated by Django 3.2.6 on 2022-01-30 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0014_job_poss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stu_details',
            name='class_10_cgpa',
        ),
    ]
