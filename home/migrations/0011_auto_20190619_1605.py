# Generated by Django 2.2.2 on 2019-06-19 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190619_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='_name',
        ),
    ]