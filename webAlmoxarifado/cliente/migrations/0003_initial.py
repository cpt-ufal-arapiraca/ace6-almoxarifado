# Generated by Django 5.0.7 on 2024-09-11 02:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('almoxarifado', '0007_log_produto'),
        ('cliente', '0002_remove_pedido_usuario_delete_itenspedido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Entregue', 'Entregue'), ('Negado', 'Negado')], default='Pendente', max_length=20)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.produto')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.pedido')),
            ],
        ),
    ]