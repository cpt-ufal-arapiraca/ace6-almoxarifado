# Generated by Django 5.1.1 on 2024-09-16 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0002_pedido_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='hora',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
