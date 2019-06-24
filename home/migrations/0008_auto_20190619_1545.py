# Generated by Django 2.2.2 on 2019-06-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_movie_releasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Awards',
            field=models.CharField(choices=[('1', 'one'), ('2', 'Two'), ('3', 'Three')], default=1, help_text='Awards won', max_length=2),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Category',
            field=models.CharField(choices=[('1', 'Thriller'), ('2', 'Action'), ('3', 'Romantic'), ('4', 'Si-Fi'), ('5', 'Comedy')], default=5, help_text='Movie Category', max_length=2),
        ),
        migrations.AlterField(
            model_name='movie',
            name='ReleaseDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]