# Generated by Django 5.1.1 on 2024-09-16 01:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0004_produto_ifcaixaqtd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='hora',
        ),
        migrations.AlterField(
            model_name='itenspedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='almoxarifado.pedido'),
        ),
    ]