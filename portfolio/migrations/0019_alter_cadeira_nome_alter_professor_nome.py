# Generated by Django 4.0.4 on 2022-05-27 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]
