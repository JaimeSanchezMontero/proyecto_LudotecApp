# Generated by Django 5.0.3 on 2024-06-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludotec_app', '0025_puntuacion_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntuacion',
            name='ganador',
            field=models.BooleanField(default=False),
        ),
    ]
