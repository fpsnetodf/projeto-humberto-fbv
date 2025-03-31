
# Generated by Django 5.1.7 on 2025-03-26 00:24

# Generated by Django 5.1.7 on 2025-03-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco', models.TextField(blank=True, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
            ]
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('contato', models.CharField(blank=True, max_length=50, null=True)),
                ('mensagem', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
