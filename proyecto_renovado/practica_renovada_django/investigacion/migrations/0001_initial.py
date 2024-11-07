# Generated by Django 5.1.3 on 2024-11-07 03:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DirectorGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('especialidad', models.CharField(blank=True, max_length=100, null=True)),
                ('laboratorio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='director_general', to='investigacion.laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('anio_fabricacion', models.IntegerField()),
                ('precio_costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='investigacion.laboratorio')),
            ],
        ),
    ]
