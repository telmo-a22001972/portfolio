# Generated by Django 4.0.4 on 2022-06-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_tfc_autor_tfc_orientador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfc_terceiros',
            name='autores',
            field=models.ManyToManyField(related_name='autores', to='portfolio.tfc_autor'),
        ),
        migrations.AlterField(
            model_name='tfc_terceiros',
            name='orientadores',
            field=models.ManyToManyField(related_name='orientadores', to='portfolio.tfc_orientador'),
        ),
    ]