# Generated by Django 4.1.6 on 2023-02-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_veiculo_estado_alter_veiculo_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='estado',
            field=models.CharField(choices=[('N', 'Novo'), ('S', 'Seminovo'), ('U', 'Usado')], max_length=1),
        ),
    ]
