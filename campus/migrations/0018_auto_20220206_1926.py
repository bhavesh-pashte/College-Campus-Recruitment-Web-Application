# Generated by Django 3.2.6 on 2022-02-06 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0017_remove_stu_details_internship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stu_details',
            name='fathers_name',
        ),
        migrations.RemoveField(
            model_name='stu_details',
            name='mothers_name',
        ),
    ]