# Generated by Django 4.2.10 on 2024-03-11 23:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_alter_estudante_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
