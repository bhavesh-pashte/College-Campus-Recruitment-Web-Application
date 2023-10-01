# Generated by Django 2.1.7 on 2019-03-15 06:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0004_stu_details_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='comp_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='*required', max_length=30)),
                ('company_name', models.CharField(help_text='*required', max_length=30)),
                ('est_year', models.CharField(help_text='*required', max_length=4)),
                ('hr_name', models.CharField(help_text='*required', max_length=30)),
                ('hr_phn', models.CharField(help_text='*required', max_length=10, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10)])),
                ('headquaters', models.CharField(help_text='*required', max_length=30)),
                ('about', models.CharField(help_text='*required', max_length=1000)),
                ('type', models.CharField(max_length=10)),
                ('email', models.EmailField(help_text='Required. Inform a valid email address.', max_length=254)),
            ],
        ),
    ]
