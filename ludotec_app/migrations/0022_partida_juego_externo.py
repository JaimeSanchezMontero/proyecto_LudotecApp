# Generated by Django 5.0.3 on 2024-05-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludotec_app', '0021_juego_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='juego_externo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
