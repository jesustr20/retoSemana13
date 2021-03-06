# Generated by Django 2.2.7 on 2019-11-09 21:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hora_funcion', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Funcion',
                'verbose_name_plural': 'Funciones',
                'ordering': ['id_pelicula'],
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=220)),
                ('tiposervicio', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('distrito', models.CharField(max_length=220)),
                ('imagen', models.ImageField(null=True, upload_to='pictures/%y')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=220, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=220, null=True)),
                ('username', models.CharField(blank=True, max_length=10, null=True)),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('fecha_venta', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_funcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.Funcion')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.Usuario')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['id_usuario'],
            },
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trailer', models.CharField(max_length=220)),
                ('titulo', models.CharField(max_length=220)),
                ('genero', models.CharField(max_length=220)),
                ('duracion', models.CharField(max_length=220)),
                ('categoria', models.CharField(max_length=220)),
                ('imagen', models.ImageField(null=True, upload_to='pictures/%y')),
                ('psinosis', models.CharField(max_length=220, null=True)),
                ('director', models.CharField(max_length=220, null=True)),
                ('idioma', models.CharField(max_length=220, null=True)),
                ('id_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.Local')),
            ],
            options={
                'verbose_name': 'Pelicula',
                'verbose_name_plural': 'Peliculas',
                'ordering': ['titulo'],
            },
        ),
        migrations.AddField(
            model_name='funcion',
            name='id_local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.Local'),
        ),
        migrations.AddField(
            model_name='funcion',
            name='id_pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.Pelicula'),
        ),
        migrations.AddField(
            model_name='funcion',
            name='id_sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.Sala'),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=220, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='pictures/%y')),
                ('id_pelicula', models.ManyToManyField(to='cine.Pelicula')),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actores',
                'ordering': ['nombre'],
            },
        ),
    ]
