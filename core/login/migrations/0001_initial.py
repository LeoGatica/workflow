# Generated by Django 3.1 on 2020-10-10 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('rut', models.CharField(max_length=15)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.EmailField(default='SOME STRING', max_length=100, unique=True, verbose_name='correo electronico')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('rol', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.rol')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
    ]