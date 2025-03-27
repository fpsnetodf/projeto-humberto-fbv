# Generated by Django 5.1.7 on 2025-03-27 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_customuser_groups_and_more'),
        ('campanha', '0003_alter_agenda_aprovado_por_alter_agenda_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='aprovado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agendas_aprovadas', to='Users.customuser', verbose_name='Aprovado por'),
        ),
    ]
