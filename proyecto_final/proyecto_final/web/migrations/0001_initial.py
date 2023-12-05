# Generated by Django 4.2.6 on 2023-12-05 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoIncidencia',
            fields=[
                ('clave_incidencia', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('incidencia', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=40)),
                ('primer_apellido', models.CharField(max_length=40)),
                ('segundo_apellido', models.CharField(max_length=40, null=True)),
                ('fecha_nac', models.DateField()),
                ('correo_electronico', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('numero_telefono', models.CharField(max_length=10)),
                ('rol', models.CharField(default='usuario', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TokenUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='TicketDeIncidencia',
            fields=[
                ('id_ticket', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=60)),
                ('comentario', models.TextField()),
                ('fecha_hora', models.DateTimeField(null=True)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ReporteDeIncidencia',
            fields=[
                ('id_reporte', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_incidencia', models.CharField(max_length=60)),
                ('calle_principal', models.CharField(max_length=40)),
                ('calle_secundaria', models.CharField(max_length=40, null=True)),
                ('fecha_de_reporte', models.DateField()),
                ('descripcion', models.TextField(null=True)),
                ('estatus', models.CharField(default='Enviado', max_length=15)),
                ('clave_de_incidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.catalogoincidencia')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.usuario')),
            ],
        ),
    ]