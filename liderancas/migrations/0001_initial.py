# Generated by Django 5.1.7 on 2025-03-31 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lideranca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('contato', models.CharField(max_length=50)),
                ('meta', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
