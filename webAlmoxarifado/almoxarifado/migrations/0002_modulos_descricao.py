# Generated by Django 5.0.7 on 2024-09-11 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulos',
            name='descricao',
            field=models.CharField(default='Descrição padrão', max_length=255),
        ),
    ]
