# Generated by Django 3.2.6 on 2022-03-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0027_auto_20220328_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_details',
            name='username',
            field=models.CharField(default='y1', help_text='enter username ex:y16it***', max_length=9),
        ),
    ]
