# Generated by Django 4.0.4 on 2022-05-27 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_user_alter_cadeira_ranking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]