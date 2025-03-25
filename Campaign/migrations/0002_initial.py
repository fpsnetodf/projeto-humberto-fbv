# Generated by Django 5.1.7 on 2025-03-24 23:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Campaign', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='aprovado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aprovacoes', to='Users.customuser'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='criado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.customuser'),
        ),
    ]
