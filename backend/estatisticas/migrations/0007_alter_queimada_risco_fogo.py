# Generated by Django 5.1.3 on 2024-12-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estatisticas', '0006_alter_queimada_dia_sem_chuva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queimada',
            name='risco_fogo',
            field=models.DecimalField(decimal_places=1, default='0.0', max_digits=5),
        ),
    ]