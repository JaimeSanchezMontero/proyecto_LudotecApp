# Generated by Django 5.0.3 on 2024-05-14 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludotec_app', '0008_alter_partida_fecha_alter_partida_juego'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionJuego',
            fields=[
                ('juego', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ludotec_app.juego')),
            ],
        ),
        migrations.AlterField(
            model_name='partida',
            name='juego',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ludotec_app.informacionjuego'),
        ),
    ]
