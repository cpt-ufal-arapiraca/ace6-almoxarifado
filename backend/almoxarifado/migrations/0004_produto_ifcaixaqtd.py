# Generated by Django 5.1.1 on 2024-09-16 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0003_alter_pedido_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='ifcaixaqtd',
            field=models.IntegerField(default=0),
        ),
    ]