# Generated by Django 2.0.3 on 2018-03-11 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='detalle_libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edicion', models.IntegerField()),
                ('num_paginas', models.IntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='disponibilidad_libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tienda', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='editorial',
            fields=[
                ('nombre', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='libro',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='modelo_extendido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apodo', models.CharField(max_length=120)),
                ('facebook', models.CharField(max_length=120)),
                ('youtube', models.CharField(max_length=120)),
                ('equipo_favorito', models.CharField(max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='disponibilidad_libro',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.libro'),
        ),
        migrations.AddField(
            model_name='detalle_libro',
            name='editorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.editorial'),
        ),
        migrations.AddField(
            model_name='detalle_libro',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.libro'),
        ),
    ]
