# Generated by Django 2.2.2 on 2019-06-20 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20190620_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='IssueDate',
            field=models.DateField(default=datetime.date.today, verbose_name='Issued'),
        ),
    ]