# Generated by Django 5.1.7 on 2025-03-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleitores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleitor',
            name='mensagem',
        ),
        migrations.AlterField(
            model_name='eleitor',
            name='contato',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
