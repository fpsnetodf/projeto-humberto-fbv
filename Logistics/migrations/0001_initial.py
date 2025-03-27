# Generated by Django 5.1.7 on 2025-03-27 17:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialCampanha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('tipo', models.CharField(choices=[('grafico', 'Material Gráfico'), ('outdoor', 'Outdoor')], max_length=50)),
                ('data_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('capacidade', models.IntegerField()),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('tipo', models.CharField(choices=[('grafico', 'Material Gráfico'), ('outdoor', 'Outdoor')], max_length=50)),
                ('data_disponivel', models.DateField()),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logistics_materials', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem', models.CharField(max_length=150)),
                ('destino', models.CharField(max_length=150)),
                ('data', models.DateField()),
                ('horario_partida', models.TimeField()),
                ('horario_chegada', models.TimeField(blank=True, null=True)),
                ('veiculo', models.CharField(max_length=100)),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
