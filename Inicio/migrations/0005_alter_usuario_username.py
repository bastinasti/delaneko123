# Generated by Django 4.0.4 on 2022-06-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0004_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Nombre de usuario'),
        ),
    ]
