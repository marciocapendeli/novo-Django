# Generated by Django 5.1 on 2024-08-18 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitante',
            name='horario_chegada',
        ),
        migrations.AlterField(
            model_name='visitante',
            name='numero_casa',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Horário de Chegada na Portaria'),
        ),
    ]
