# Generated by Django 2.2.2 on 2019-06-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190619_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Awards',
            field=models.CharField(choices=[(1, 'one'), (2, 'Two'), (3, 'Three')], default=1, help_text='Awards won', max_length=2),
        ),
    ]