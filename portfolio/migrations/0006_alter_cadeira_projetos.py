# Generated by Django 4.0.4 on 2022-05-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_rename_professor_praticas_cadeira_professor_pratica_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='projetos',
            field=models.ManyToManyField(to='portfolio.projeto'),
        ),
    ]
