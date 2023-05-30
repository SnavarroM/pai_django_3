# Generated by Django 3.0.6 on 2023-05-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=50, verbose_name='Descripción Cargo')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
    ]