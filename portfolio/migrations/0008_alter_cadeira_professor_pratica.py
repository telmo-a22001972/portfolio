# Generated by Django 4.0.4 on 2022-05-24 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_cadeira_projetos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='professor_pratica',
            field=models.ManyToManyField(related_name='professor_pratica', to='portfolio.professor'),
        ),
    ]
